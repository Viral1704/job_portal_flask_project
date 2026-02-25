from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db

from app.models.user import User
from app.models.job import Job


job_bp = Blueprint('job', __name__)


@job_bp.route('/jobs', methods = ['POST'])
@jwt_required()
def create_job():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message' : 'User not found!'}), 404
    
    if user.role != 'recruiter':
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({"message": "Title is required"}), 400
    
    description = data.get('description')
    if not description:
        return jsonify({"message": "Description is required"}), 400
    
    company = data.get('company')
    if not company:
        return jsonify({"message": "Company is required"}), 400
    
    location = data.get('location')
    
    salary_min = data.get('salary_min')
    salary_max = data.get('salary_max')

    if salary_min and salary_max:
        if salary_min > salary_max:
            return jsonify({"message": "Minimum salary cannot be greater than maximum salary"}), 400

    experience_level = data.get('experience_level', 'junior')
    if experience_level not in ['junior', 'mid', 'senior']:
        return jsonify({"message": "Invalid experience level value"}), 400


    new_job = Job(
        title = title,
        description = description,
        company = company,
        location = location,
        salary_min = salary_min,
        salary_max = salary_max,
        experience_level = experience_level,
        status = 'open',
        recruiter_id = user.id
    )
    
    db.session.add(new_job)
    db.session.commit()

    return jsonify({'message' : 'Job created successfully!'}), 201



@job_bp.route('/jobs/me', methods=['GET'])
@jwt_required()
def get_my_jobs():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    if user.role != 'recruiter':
        return jsonify({"message": "Unauthorized"}), 403
    
    jobs = Job.query.filter_by(recruiter_id= user.id).all()

    jobs_data = []
    for job in jobs:
        jobs_data.append({
            'id' : job.id,
            'title' : job.title,
            'description' : job.description,
            'company' : job.company,
            'location' : job.location,
            'salary_min' : job.salary_min,
            'salary_max' : job.salary_max,
            'experience_level' : job.experience_level,
            'status' : job.status
        })

    return jsonify({'jobs' : jobs_data}), 200