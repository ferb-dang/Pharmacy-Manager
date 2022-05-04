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
    id: int

# Những nhãn thuốc được update


class MedicinesUpdate (MedicinesBase):
    pass


class Medicines (BaseModel):
    id: int
