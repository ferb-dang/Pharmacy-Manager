from sqlalchemy import Integer, String, Column, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.base import Base


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
    )  # Thiết lập kết nối bảng "tbl_users" với "tbl_roles"

    @classmethod
    def create(cls, obj: any):
        translate = cls()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        return translate