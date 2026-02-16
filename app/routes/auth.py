from flask import Blueprint, request, jsonify

from app.models.user import User

from flask_jwt_extended import create_access_token, create_refresh_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message' : 'Email and password are required'}), 400
    
    user = User.query.filter_by(email = email).first()
    if user is None or not user.verify_password(password):
        return jsonify({'message' : 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity = user.id)
    refresh_token = create_refresh_token(identity = user.id)

    return jsonify({
        'access_token' : access_token,
        'refresh_token' : refresh_token
    }), 200