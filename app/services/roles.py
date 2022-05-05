from dbmodels import Roles
from .base import BaseService


class MedicineService(BaseService[Roles]):
    pass

medicine_services = MedicineService(Roles) #get_one and get_all and delete_one

