from dbmodels import Medicines
from .base import BaseService, Session
from models import MedicinesCreate, MedicinesUpdate


class MedicineService(BaseService[Medicines]):
    pass

medicine_services = MedicineService(Medicines) #get_one and get_all

def get_by_name(session: Session, name: str):
    return session.query(Medicines).filter(Medicines.name == name).first()

def create(session: Session, medicine: MedicinesCreate):
    db_create_medicine = Medicines.create(medicine)
    session.add(db_create_medicine)
    session.commit()
    session.refresh(db_create_medicine)
    return db_create_medicine

def update(session: Session, mec: Medicines, mecdicine_schemas: MedicinesUpdate):
    update_data = mecdicine_schemas.dict()
    for k in mec:
        if k in update_data:
            setattr(mec, k , update_data[k])
    session.add(mec)
    session.commit()
    session.close(mec)
    return mec

    