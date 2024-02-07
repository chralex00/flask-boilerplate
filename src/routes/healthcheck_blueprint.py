from flask import Blueprint
from controllers.healthcheck import healthcheck

healthcheck_blueprint = Blueprint('healthcheck_blueprint', __name__)

healthcheck_blueprint.route('/healthcheck', methods = ['GET'])(healthcheck)