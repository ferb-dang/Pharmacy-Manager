from dbmodels import Permissions
from .base import BaseService


class MedicineService(BaseService[Permissions]):
    pass

medicine_services = MedicineService(Permissions) #get_one and get_all and delete_one

