from dbmodels import Users
from .base import BaseService, Session
from core import password_hash


class UserService(BaseService[Users]):
    def check_exist_user(self, session: Session, user_name: str, password: str):
        return session.query(Users).filter(Users.user_name==user_name, Users.password==password).first()

    def check_user_name(self, session: Session, user_name: str):
        return session.query(Users).filter(Users.user_name == user_name).first()

    def check_phone_number(self, session: Session, phone: str):
        return session.query(Users).filter(Users.phone_numbers == phone).first()

    def create_user(self, session: Session, obj: any):
        obj = super().create_one_temp(session, obj)
        obj.password = password_hash(obj.password)
        obj = self.save(session, obj)
        return obj


user_services = UserService(Users)  # get_one and get_all and delete_one
