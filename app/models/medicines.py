from datetime import date
from pydantic import BaseModel


# Những nhãn thuốc được đọc từ db
class MedicinesBase (BaseModel):
    id: int = None
    name: str = None
    medical_function: str = None
    quantity: int = None
    price: str = None

    class Config:
        orm_mode = True

# Nhãn thuốc được tạo ra


class MedicinesCreate (MedicinesBase):
    name: str
    medical_function: str
    price: str

# Những nhãn thuốc được update


class MedicinesUpdate (MedicinesBase):
    id: int
    name: str
    medical_function: str
    quantity: int
    price: str
    manufacture_date: date
    expire_date: date
    status: str


class Medicines (BaseModel):
    id: int
