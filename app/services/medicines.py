from dbmodels import Medicines
from .base import BaseService, Session
from models import MedicinesCreate, MedicinesUpdate


class MedicineService(BaseService[Medicines]):
    pass

medicine_services = MedicineService(Medicines) #get_one and get_all and delete_one

def get_by_name(session: Session, name: str):
    return session.query(Medicines).filter(Medicines.name == name).first()


# def update(session: Session, mec: Medicines, mecdicine_schemas: MedicinesUpdate):
#     update_data = mecdicine_schemas.dict()
#     for k in update_data:
#         if k in update_data:
#           setattr(mec, k , update_data[k])
#     session.add(mec)
#     session.commit()
#     session.refresh(mec)
#     return mec

    