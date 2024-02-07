import os
from database.database_init import get_database_connection

def create_one(person):
    connection = get_database_connection(os.getenv('DATABASE_NAME'))
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO people (first_name, last_name, birthday_year, gender, email) VALUES (?, ?, ?, ?, ?)',
        (person["first_name"], person["last_name"], person["birthday_year"], person["gender"], person["email"])
    )
    connection.commit()
    connection.close()

def find_one_by_id(id):
    connection = get_database_connection(os.getenv('DATABASE_NAME'))
    personFound = connection.execute(f"SELECT * FROM people WHERE id = {id}").fetchone()
    connection.close()
    return personFound

def find_all():
    connection = get_database_connection(os.getenv('DATABASE_NAME'))
    peopleFound = connection.execute(f"SELECT * FROM people").fetchall()
    connection.close()
    return peopleFound

def update_one(id, person):
    connection = get_database_connection(os.getenv('DATABASE_NAME'))
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE people SET first_name = ?, last_name = ?, birthday_year = ?, gender = ?, email = ? WHERE id = ?',
        (person["first_name"], person["last_name"], person["birthday_year"], person["gender"], person["email"], id)
    )
    connection.commit()
    connection.close()

def delete_one_by_id(id):
    connection = get_database_connection(os.getenv('DATABASE_NAME'))
    cursor = connection.cursor()
    cursor.execute('DELETE FROM people WHERE id = ?', (id))
    connection.commit()
    connection.close()