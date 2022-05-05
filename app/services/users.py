from dbmodels import Users
from .base import BaseService,Session


class UserService(BaseService[Users]):
    pass

user_services = UserService(Users) #get_one and get_all and delete_one

def get_by_phone_number(session: Session, phone: str):
    return session.query(Users).filter(Users.phone_numbers == phone).first()