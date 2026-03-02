from app.models.job import Job

from app.models.application import Application

from app.extensions import db


def apply_to_job(user, job_id):
    
    job = Job.query.get(job_id)

    if not job:
        raise LookupError('Job not found!')

    if job.status != 'open':
        raise ValueError('Job is not open for applications!')

    existing_application = Application.query.filter_by(candidate_id=user.id, job_id=job.id).first()

    if existing_application:
        raise ValueError('You have already applied to this job!')

    application = Application(
        candidate_id = user.id,
        job_id = job.id,
        status = 'applied'
    )

    db.session.add(application)
    db.session.commit()   
    
    return application





def update_application_status(user, application_id, new_status):
    
    application = Application.query.get(application_id)

    if not application:
        raise LookupError('Application not found!')
    
    if application.job.recruiter_id != user.id:
        raise PermissionError('You do not have permission!')
    
    if application.status != 'pending':
        raise ValueError('Status must be pending!')
    
    if new_status not in ['accepted', 'rejected']:
        raise ValueError('Invalid status value!')
    
    application.status = new_status

    db.session.commit()

    return application