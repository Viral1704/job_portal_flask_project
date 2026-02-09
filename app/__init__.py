from flask import Flask

from .extensions import db, jwt, migrate

from .config import Config

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    jwt.init_app(app)


    from app.models.user import User
    from app.models.job import Job
    from app.models.application import Application

    return app



