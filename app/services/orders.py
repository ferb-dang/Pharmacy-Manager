from sqlalchemy.orm import Session

from dbmodels import Orders, Medicines
from models import OrdersCreate, Orders as ods
from .base import BaseService
from core.security import decode_jwt


class OrderService(BaseService[Orders]):
    def get_order(self, session: Session, obj: any):
        payload = decode_jwt(obj)
        if payload['role'] == '4':
            return session.query(ods).filter(ods.user_id == payload['user_id']).all()
        else: 
            return session.query(ods).all()



    def create_one(self, session: Session, obj: OrdersCreate, user_id: int, autocommit=True):
        instance: Orders = super().create_one(session, obj, False)
        instance.user_id = user_id
        medicine_lists = session.query(Medicines).filter(Medicines.id.in_(obj.medicine_order)).all()
        instance.medicines = medicine_lists

        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance


order_services = OrderService(Orders)  # get_one and get_all and delete_one
