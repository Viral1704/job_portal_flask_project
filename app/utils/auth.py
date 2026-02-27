from app.models.user import User

from flask_jwt_extended import get_jwt_identity

def get_current_user():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        raise LookupError('User not found!')
    
    return user


def require_role(user, required_role):
    if user.role != required_role:
        raise PermissionError(f"{required_role.capitalize()} role required")