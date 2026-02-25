from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db
from app.models.user import User
from app.models.application import Application
from app.models.job import Job

application_bp = Blueprint('application', __name__)


@application_bp.route('/applications', methods=['POST'])
@jwt_required()
def apply():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if user.role != 'applicant':
        return jsonify({'error': 'Only applicants can apply for jobs'}), 403
    

    data = request.get_json() or {}

    job_id = data.get('job_id')
    if not job_id:
        return jsonify({'error': 'Job ID is required'}), 400
    
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    
    if job.status != 'open':
        return jsonify({'error': 'Job is not open for applications'}), 400
    
    existing_application = Application.query.filter_by(candidate_id = user.id, job_id = job.id).first()
    if existing_application:
        return jsonify({'error': 'You have already applied for this job'}), 400
    
    application = Application(candidate_id = user.id, job_id = job.id, status = 'applied')

    db.session.add(application)
    db.session.commit()

    return jsonify({'message': 'Application submitted successfully'}), 201