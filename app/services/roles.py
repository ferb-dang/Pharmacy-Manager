from dbmodels import Roles
from .base import BaseService


class MedicineService(BaseService[Roles]):
    pass

medicine_services = MedicineService(Roles)

