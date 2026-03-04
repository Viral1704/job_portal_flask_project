import os

class Config:

    SECRET_KEY = os.getenv('SECRET_KEY')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///job_portal.db') # this is sqlite database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') # this is postgresql database
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DEBUG = os.getenv('DEBUG', 'False') == 'True'