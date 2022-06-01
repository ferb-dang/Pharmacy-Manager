from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from db.base import Base
from .role_permission_association import role_permission


# create database "tbl_roles"
class Roles(Base):
    __tablename__ = "tbl_roles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    slug = Column(String(50))
    permissions = relationship(
        "Permissions", secondary=role_permission
    )  # Setting connection tbl_permissions with tbl_role_permission
