from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db') # Creating DB connection

def connect_db():
    connection = engine.connect() # Establishing connection to the database
    return connection



