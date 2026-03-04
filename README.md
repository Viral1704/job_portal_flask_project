Job Portal Backend API

A RESTful backend API for a job portal platform where recruiters can create job postings and applicants can apply to jobs.

The system handles authentication, role-based access control, job applications, and recruiter workflows.

This project demonstrates backend development concepts such as API design, authentication, database relationships, pagination, filtering, and production deployment.

Tech Stack

Python

Flask

PostgreSQL

SQLAlchemy

Flask-JWT-Extended

Flask-Migrate (Alembic)

Gunicorn

Render (Deployment)

Features
Authentication

User registration

User login

JWT authentication

Access tokens

Role-Based Access Control

Two roles are supported:

Recruiter

Create job postings

View applicants for their jobs

Update application status

Applicant

Apply for jobs

View jobs they have applied to

Job Management

Recruiters can create job listings containing:

Job title

Description

Company

Location

Salary range

Experience level

Job status

Application System

Applicants can apply to jobs.

The system ensures:

A job must be open before applying

Duplicate applications are prevented

Recruiters can view applicants for their jobs

Recruiters can update application status

Application status flow:

pending → accepted / rejected
Pagination & Filtering

The API supports pagination and filtering.

Example:

GET /applications/me?page=1&per_page=10
GET /applications/me?status=accepted
Database

The project uses PostgreSQL.

Main tables:

users

jobs

applications

Relationships:

A recruiter can create multiple jobs

A job can receive multiple applications

An applicant can apply to multiple jobs

Database migrations are managed using Flask-Migrate (Alembic).

Live API

Base URL

https://job-portal-flask-project.onrender.com
API Endpoints
Authentication

Register User

POST /auth/register

Login

POST /auth/login
Jobs

Create Job (Recruiter)

POST /jobs

Get Recruiter's Jobs

GET /jobs/me

Get Applicants for a Job

GET /jobs/<job_id>/applicants
Applications

Apply to Job

POST /applications

Get My Applications

GET /applications/me

Update Application Status (Recruiter)

PATCH /applications/<application_id>
Screenshots
Live API Response

Example response from the deployed API.
![API Response](images/api_response.png)

Database Tables

PostgreSQL tables used in the system.

users

jobs

applications
![API Response](images/database_tables.png)

Project Structure
job_portal_flask_project
│
├── app
│   ├── models
│   ├── routes
│   ├── services
│   ├── utils
│   ├── extensions.py
│   ├── config.py
│   └── __init__.py
│
├── migrations
├── run.py
├── requirements.txt
└── README.md
Running the Project Locally

Clone the repository

git clone https://github.com/Viral1704/job_portal_flask_project.git

Move into the project directory

cd job_portal_flask_project

Create a virtual environment

python -m venv venv

Activate it

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Create a .env file

Example:

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=postgresql://user:password@localhost:5432/job_portal

Run database migrations

flask db upgrade

Run the server

flask run
Deployment

The project is deployed on Render using:

Gunicorn

PostgreSQL

Environment variables

Live API:

https://job-portal-flask-project.onrender.com
Author

Viral Vaghasiya

GitHub
https://github.com/Viral1704