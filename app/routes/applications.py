from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required

from app.extensions import db
from app.models.user import User
from app.models.application import Application
from app.models.job import Job

from app.services.application_service import apply_to_job

from app.utils.auth import get_current_user, require_role

application_bp = Blueprint('application', __name__)


@application_bp.route('/applications', methods=['POST'])
@jwt_required()
def apply():

    user = get_current_user()
    require_role(user, "applicant")
    
    data = request.get_json() or {}

    job_id = data.get('job_id')
    if not job_id:
        return jsonify({'error': 'Job ID is required'}), 400
    
    try:
        application = apply_to_job(user, job_id)
    except LookupError as e:
        return jsonify({"error": str(e)}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({'message': 'Application submitted successfully', 'application_id' : application.id}), 201



@application_bp.route('/applications/me', methods = ['GET'])
@jwt_required()
def get_my_applications():
    
    user = get_current_user()
    require_role(user, "applicant")
    
    applications = user.applications.all()

    application_data = []

    for application in applications:
        job = application.job
        application_data.append({
            'job_title' : job.title,
            'job_description' : job.description,
            'job_location' : job.location,
            'job_status' : job.status,
            'job_created_at' : job.created_at.isoformat(),
            'application_status' : application.status,
            'applied_at' : application.created_at.isoformat()
        })

    return jsonify({'applications' : application_data}), 200