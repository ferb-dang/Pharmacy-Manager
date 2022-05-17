# from sqlalchemy import create_engine,MetaData,engine
# from sqlalchemy.orm import sessionmaker
# from main import app
# from unittest import TestCase
# from fastapi.testclient import TestClient


# from core.config import DB_TEST_STRING

# session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# class EngineTestCase (TestCase):
#     meta = MetaData()
#     engine = create_engine(DB_TEST_STRING)
#     client = TestClient(app)

#     def setUp(self) -> None:
#         self.token=""
    
#     def tearDown(self) -> None:
#         ...


