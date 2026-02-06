from app.extensions import db


class Job(db.Model):

    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False, index = True)
    description = db.Column(db.Text, nullable = False)
    comapny = db.Column(db.String(100), nullable = False, index = True)
    location = db.Column(db.String(50), nullable = True, index = True)
    salary_min = db.Column(db.Integer, nullable = True)
    salary_max = db.Column(db.Integer, nullable = True)
    experience_level = db.Column(db.String(50), nullable = False, default = 'junior', index = True)
    job_type = db.Column(db.String(50), nullable = False, default = 'full-time', index = True)
    status = db.Column(db.String(50), nullable = False, default = 'open', index = True)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    created_at = db.Column(db.DateTime, default = db.func.now(), nullable = False) # This will automatically set the timestamp when the record is created
    updated_at = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now(), nullable = False) # This will automatically update the timestamp whenever the record is updated
