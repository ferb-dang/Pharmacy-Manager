from unicodedata import name
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import MedicinesBase, Medicines, MedicinesCreate, MedicinesUpdate
from services import medicine_services, create, update, get_by_name
from db.engine import create_session

router = APIRouter()

@router.get("/medicines", tags=["medicine"], response_model=list[MedicinesBase])
def read_medicines(skip: int = 0, limit: int = 200, session: Session= Depends(create_session)):
    medicines = medicine_services.get_all(session, skip=skip, limit=limit)
    return medicines

@router.get("/medicine/{id}", tags=["medicine"], response_model=MedicinesBase)
def read_medicine(id: int, session: Session=Depends(create_session)):
    medicine = medicine_services.get_one(session,id)
    return medicine

@router.post("/", response_model=Medicines)
def create_medicine_by_id(medicine_schemas: MedicinesCreate,session: Session=Depends(create_session)):
    medicine = get_by_name(session, name = medicine_schemas.name)
    if medicine:
        raise HTTPException(status_code=400, detail="Đã tồn tại tên thuốc này.")
    
    medicine= create(session, medicine=medicine)
    return medicine

@router.put("/medicine", response_model= Medicines)
def update_medicine(mec: Medicines, mecdicine_schemas: MedicinesUpdate,session: Session=Depends(create_session)):
    medicine = update(session, mec=mec, mecdicine_schemas=mecdicine_schemas)
    return medicine

@router.delete("/mecdicine/{id}", response_model= Medicines)
def delete_medicine(id: int, session: Session=Depends(create_session)):
    medicine = medicine_services.get_one(session,id)
    if medicine:
        session.delete(medicine)
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"medicine with id {id} not found"
        )

    return f"Đã xóa thành công id thuốc là {id}"