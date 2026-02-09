from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False, index = True)
    password_hash = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(75), unique = True, index = True, nullable = True)
    role = db.Column(db.String(50), nullable = False, default = 'applicant', index = True)
    status = db.Column(db.String(50), nullable = False, default = 'active', index = True)
    created_at = db.Column(db.DateTime, default = db.func.now(), nullable = False) # This will automatically set the timestamp when the record is created
    updated_at = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now(), nullable = False) # This will automatically update the timestamp whenever the record is updated

    applications = db.relationship(
        'Application', 
        backref = 'candidate', 
        lazy = 'dynamic'
        )

    jobs = db.relationship(
        'Job', 
        backref = 'recruiter', 
        lazy = 'dynamic'
        )
    

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)