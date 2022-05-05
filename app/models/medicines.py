from datetime import date
from pydantic import BaseModel


#You can read data from these models
class MedicinesBase (BaseModel):
    name: str = None
    medical_function: str = None
    quantity: int = None
    price: str = None

    class Config:
        orm_mode = True

#FastApi will using these models to create data
class MedicinesCreate (MedicinesBase):
    id: int
    manufacture_date: date
    expire_date: date
    status: str

#FastApi will using these models to update data
class MedicinesUpdate (MedicinesBase):
    manufacture_date: date
    expire_date: date
    status: str

class Medicines (MedicinesBase):
    id: int 
