from db.engine import engine
import dbmodels



print("Successfully create database")
dbmodels.Base.metadata.create_all(engine)
#Create database using SQLAlchemy models
