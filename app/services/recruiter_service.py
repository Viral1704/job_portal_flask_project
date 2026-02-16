from app.models.job import Job


def get_recruiter_dashboard_data(user):
    if user.role != 'recruiter':
        raise PermissionError("User does not have recruiter role")
    
    jobs = Job.query.filter_by(recruiter_id=user.id).all()

    dashboard_data = []
    for job in jobs:
        dashboard_data.append({
            'job_id' : job.id,
            'title' : job.title,
            'status' : job.status,
            'application_count' : job.applications.count()
        })

    
    return dashboard_data