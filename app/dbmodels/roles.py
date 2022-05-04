from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from db.base import Base 
from .role_permission_association import role_permission

class Roles(Base):
    __tablename__ = "tbl_roles"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    slug = Column(String(50))
    permissions = relationship(
        "Permissions", secondary=role_permission
    )  # Thiết lập kết nối đến với bảng tbl_permissions thông qua bảng trung gian tbl_role_permission

    @classmethod
    def create(cls, obj: any):
        translate = cls()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        return translate