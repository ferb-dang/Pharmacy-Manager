from sqlalchemy import Integer, String, Column, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.base import Base


# create database "tbl_users"
class Users(Base):
    __tablename__ = "tbl_users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    role_id = Column(Integer, ForeignKey("tbl_roles.id"), nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    gender = Column(Integer)
    date_of_birth = Column(Date)
    email = Column(String(100))
    address = Column(String(500))
    phone_numbers = Column(String(20))
    roles = relationship(
        "Roles", backref="users"
    )  # Create database connection "tbl_users" with "tbl_roles"
