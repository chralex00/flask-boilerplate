from flask import current_app as app
import daos.person as PersonDao
from datetime import datetime

def create_one(person):
    try:
        app.logger.info(f"PersonService: Creating new person...")
        PersonDao.create_one(person)
        app.logger.info(f"PersonService: person created!")
    except Exception as exception:
        app.logger.info(f"PersonService: create_one terminated with error at {datetime.today()}")
        app.logger.info(f"PersonService: exception is {exception}")
        raise exception
        

def find_one(id):
    try:
        app.logger.info(f"PersonService: finding a person by ID {id}...")
        personFound = PersonDao.find_one_by_id(id)
        if personFound != None:
            app.logger.info(f"Person with id {id} found!")
        else:
            app.logger.info(f"Person with id {id} not found!")
        return personFound
    except Exception as exception:
        app.logger.info(f"PersonService: find_one terminated with error at {datetime.today()}")
        app.logger.info(f"PersonService: exception is {exception}")
        raise exception

def find_all():
    try:
        app.logger.info(f"PersonService: finding all people...")
        peopleFound = PersonDao.find_all()
        app.logger.info(f"PersonService: people found!")
        return peopleFound
    except Exception as exception:
        app.logger.info(f"PersonService: find_all terminated with error at {datetime.today()}")
        app.logger.info(f"PersonService: exception is {exception}")
        raise exception

def update_one(id, person):
    try:
        app.logger.info(f"PersonService: updating a person by ID {id}...")
        PersonDao.update_one(id, person)
        app.logger.info(f"PersonService: person updated!")
    except Exception as exception:
        app.logger.info(f"PersonService: update_one terminated with error at {datetime.today()}")
        app.logger.info(f"PersonService: exception is {exception}")
        raise exception

def delete_one(id):
    try:
        app.logger.info(f"PersonService: deleting a person by ID {id}...")
        PersonDao.delete_one_by_id(id)
        app.logger.info(f"PersonService: person with id {id} deleted!")
    except Exception as exception:
        app.logger.info(f"PersonService: update_one terminated with error at {datetime.today()}")
        app.logger.info(f"PersonService: exception is {exception}")
        raise exception