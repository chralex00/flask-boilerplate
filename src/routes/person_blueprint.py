from flask import Blueprint
import controllers.person as PersonController

person_blueprint = Blueprint('person_blueprint', __name__)

person_blueprint.route('/people', methods = ['POST'])(PersonController.create_one)
person_blueprint.route('/people/<id>', methods = ['GET'])(PersonController.find_one)
person_blueprint.route('/people', methods = ['GET'])(PersonController.find_all)
person_blueprint.route('/people/<id>', methods = ['PUT'])(PersonController.update_one)
person_blueprint.route('/people/<id>', methods = ['DELETE'])(PersonController.delete_one)