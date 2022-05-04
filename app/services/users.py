from dbmodels import Users
from .base import BaseService


class MedicineService(BaseService[Users]):
    pass

medicine_services = MedicineService(Users)

