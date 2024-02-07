from sqlite3 import connect, Row

INIT_DATABASE_SCRIPT_NAME = "sql-init.sql"

def database_init(database_name):
    connection = connect(database_name)
    with open(INIT_DATABASE_SCRIPT_NAME) as init_script:
        connection.executescript(init_script.read())
    connection.commit()
    connection.close()

def get_database_connection(database_name):
    connection = connect(database_name)
    connection.row_factory = Row
    return connection
