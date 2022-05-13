from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base
from .order_medicine_association import order_medicine

# Create database "tbl_orders"
class Orders(Base):
    __tablename__ = "tbl_orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
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
