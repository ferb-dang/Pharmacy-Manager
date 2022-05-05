from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:nam1ahai@localhost/dbo_pharmacy")
# Create database engine


session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Create new "session" to db when being called

def create_session(): #Each time, a session is being generate, they will execute, then close..... then generate a new one -> repeat
    db = session_local()
    try:
        yield db
    finally:
        db.close()
