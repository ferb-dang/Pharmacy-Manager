from dbmodels import Orders
from .base import BaseService


class MedicineService(BaseService[Orders]):
    pass

medicine_services = MedicineService(Orders)

