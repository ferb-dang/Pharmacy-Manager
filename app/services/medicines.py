from dbmodels import Medicines
from .base import BaseService, Session


class MedicineService(BaseService[Medicines]):
    pass

medicine_services = MedicineService(Medicines) #get_one and get_all and delete_one

def get_by_name(session: Session, name: str):
    return session.query(Medicines).filter(Medicines.name == name).first()

