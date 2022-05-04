from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base
from .order_medicine_association import order_medicine


class Orders(Base):
    __tablename__ = "tbl_orders"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.id"), nullable=False)
    status = Column(String(500))
    shipping_address = Column(String(500))
    shipping_fee = Column(String(30))
    users = relationship(
        "Users", backref="orders"
    )  # Thiết lập kết nối bảng "tbl_users" với "tbl_orders"
    medicines = relationship(
        "Medicines", secondary=order_medicine, back_populates="orders"
    )

    @classmethod
    def create(cls, obj: any):
        translate = cls()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        return translate