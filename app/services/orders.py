from dbmodels import Orders
from .base import BaseService


class MedicineService(BaseService[Orders]):
    pass

medicine_services = MedicineService(Orders) #get_one and get_all and delete_one

