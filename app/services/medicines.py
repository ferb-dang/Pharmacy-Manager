from dbmodels import Medicines
from .base import BaseService


class MedicineService(BaseService[Medicines]):
    pass

medicine_services = MedicineService(Medicines)

