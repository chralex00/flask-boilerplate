import os

def check_env_variables():
    print(f"Checking environment variables...")

    error_messages  = []

    LISTENING_PORT = os.getenv('LISTENING_PORT')
    if (LISTENING_PORT is None):
        error_messages.append("LISTENING_PORT is a required variable")
    elif (not (LISTENING_PORT.isdigit() and int(LISTENING_PORT) >= 1024 and int(LISTENING_PORT) <= 65535)):
        error_messages.append("LISTENING_PORT must be an integer number between 1024 and 65535")

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    if (DATABASE_NAME is None):
        error_messages.append("DATABASE_NAME is a required variable")
    elif (not (len(DATABASE_NAME) >= 4 and len(DATABASE_NAME) <= 256 )):
        error_messages.append("DATABASE_NAME must be a string between 4 and 256 characters")

    if (len(error_messages) > 0):
        print("[")
        for error_message in error_messages:
            print(f"\t{error_message}")
        print("]")
        
        print(f"Wrong configuration: please, set correct values for all environment variables")
        
        exit()
    else:
        print("[")
        print(f"\tLISTENING_PORT = {LISTENING_PORT}")
        print(f"\tDATABASE_NAME = {DATABASE_NAME}")
        print("]")
        print(f"Good configuration!")