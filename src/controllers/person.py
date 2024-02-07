from flask import Response, request, current_app as app, json
from datetime import datetime
import services.person as PersonService
from dtos.CreateUpdatePersonDto import CreateUpdatePerson
from marshmallow import ValidationError

def create_one():
    try:
        app.logger.info(f"PersonController: POST /api/people API called at {datetime.today()}")

        person = CreateUpdatePerson().load(request.json)
        PersonService.create_one(person)

        return Response(response = {}, status = 201, mimetype = 'application/json')
    except ValidationError as validationError:
        return Response(response = json.dumps(validationError.messages), status = 400, mimetype = 'application/json')
    except Exception as exception:
        app.logger.info(f"PersonController: POST /api/people API terminated with exception at {datetime.today()}")
        return Response(response = {}, status = 500, mimetype = 'application/json')

def find_one(id):
    try:
        app.logger.info(f"PersonController: GET /api/people/{id} API called at {datetime.today()}")
        
        row = PersonService.find_one(id)

        if (row is None):
            return Response(response = {}, status = 404, mimetype = 'application/json')
        
        personFound = dict(row)
        
        return Response(response = json.dumps(personFound), status = 200, mimetype = 'application/json')
    except:
        app.logger.info(f"PersonController: GET /api/people/{id} API terminated with exception at {datetime.today()}")
        return Response(response = {}, status = 500, mimetype = 'application/json')

def find_all():
    try:
        app.logger.info(f"PersonController: GET /api/people API called at {datetime.today()}")
        
        rows = PersonService.find_all()
        
        peopleFound = [dict(row) for row in rows]
        
        return Response(response = json.dumps(peopleFound), status = 200, mimetype = 'application/json')
    except Exception as exception:
        app.logger.info(f"PersonController: GET /api/people API terminated with exception at {datetime.today()}")
        print(f"exception is {exception}")
        return Response(response = {}, status = 500, mimetype = 'application/json')

def update_one(id):
    try:
        app.logger.info(f"PersonController: PUT /api/people/{id} API called at {datetime.today()}")

        person = CreateUpdatePerson().load(request.json)

        row = PersonService.find_one(id)
        if (row is None):
            return Response(response = {}, status = 404, mimetype = 'application/json')

        PersonService.update_one(id, person)
        
        return Response(response = {}, status = 200, mimetype = 'application/json')
    except ValidationError as validationError:
        return Response(response = json.dumps(validationError.messages), status = 400, mimetype = 'application/json')
    except:
        app.logger.info(f"PersonController: PUT /api/people/{id} API terminated with exception at {datetime.today()}")
        return Response(response = {}, status = 500, mimetype = 'application/json')

def delete_one(id):
    try:
        app.logger.info(f"PersonController: DELETE /api/people/{id} API called at {datetime.today()}")
        
        row = PersonService.find_one(id)
        if (row is None):
            return Response(response = {}, status = 404, mimetype = 'application/json')
        
        PersonService.delete_one(id)
        
        return Response(response = {}, status = 200, mimetype = 'application/json')
    except:
        app.logger.info(f"PersonController: DELETE /api/people/{id} API terminated with exception at {datetime.today()}")
        return Response(response = {}, status = 500, mimetype = 'application/json')