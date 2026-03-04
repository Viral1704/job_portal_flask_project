import os

class Config:

    SECRET_KEY = os.getenv('SECRET_KEY')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    DATABASE_URL = os.getenv('DATABASE_URL')

    # Render give database url start with postgres but for sqlalchemy we need postgresql.
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = os.getenv('DEBUG', 'False') == 'True'