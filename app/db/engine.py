from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:nam1ahai@localhost/dbo_pharmacy")
# Tạo database

# "phiên dịch" những cấu hình của hàm Session()
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
