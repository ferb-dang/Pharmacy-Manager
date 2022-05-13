from db.engine import engine, text
import dbmodels
import os



print("Successfully create database")
dbmodels.Base.metadata.create_all(engine)
#Create database using SQLAlchemy models


with engine.connect() as con:
    filename = os.path.join(os.getcwd(),'db','permission.sql')
    with open(filename) as file:
        query = text(file.read())
        con.execute(query)