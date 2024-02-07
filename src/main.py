from flask import Flask
import logging
import os
from dotenv import load_dotenv
from waitress import serve
from routes.healthcheck_blueprint import healthcheck_blueprint
from routes.person_blueprint import person_blueprint
from database.database_init import database_init
from check_env_variables import check_env_variables

def create_app():
    load_dotenv()
    check_env_variables()
    database_init(os.getenv('DATABASE_NAME'))

    app = Flask(__name__)

    app.register_blueprint(healthcheck_blueprint, url_prefix = '/api')
    app.register_blueprint(person_blueprint, url_prefix = '/api')

    app.logger.setLevel(logging.INFO)
    app.logger.info(f"Database {os.getenv('DATABASE_NAME')} (re)initzialized")
    app.logger.info(f"Service {os.getenv('DOCKER_CONTAINER_NAME')} started")
    app.logger.info(f"Service listening on port {os.getenv('LISTENING_PORT')}")

    serve(app, host = "0.0.0.0", port = os.getenv('LISTENING_PORT'))
    
    return app

create_app()