from app.extensions import db

class Application(db.Model):
    __tablename__ = 'applications'

    __table_args__ = (
        db.UniqueConstraint('job_id', 'candidate_id', name='uq_job_candidate'),
    )

    id = db.Column(db.Integer, primary_key = True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable = False, index = True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False, index = True)
    status = db.Column(db.String(20), nullable = False, default = 'applied', index = True)
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.now())
    updated_at = db.Column(db.DateTime, nullable = False, default = db.func.now(), onupdate = db.func.now())