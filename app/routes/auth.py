from flask import Blueprint, request, jsonify

from app.models.user import User

from flask_jwt_extended import create_access_token, create_refresh_token

from app.extensions import db

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






@auth_bp.route('/register', methods = ['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not name or not username or not email or not password:
        return jsonify({'message' : 'Name, username, email and password are required'}), 400
    
    if User.query.filter_by(username = username).first():
        return jsonify({'message' : 'Username already exists!'}), 400
    
    if User.query.filter_by(email = email).first():
        return jsonify({'message' : 'Email already exists!'}), 400
    
    new_user = User(name = name, username = username, email = email)

    new_user.password = password

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'User registered successfully', 'user_id' : new_user.id}), 201
