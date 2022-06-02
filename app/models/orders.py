from pydantic import BaseModel
from typing import List, Optional


# You can read data from these models
class OrdersBase(BaseModel):
    status: Optional[str] = None
    shipping_address: Optional[str] = None
    shipping_fee: Optional[str] = None

    class Config:
        orm_mode = True


# FastApi will using these models to create data
class OrdersCreate(OrdersBase):
    medicine_order: List = None


# FastApi will using these models to update order fee and address
class OrdersUpdate(OrdersBase):
    pass


# FastApi will using these models to update status
class OrdersStatusUpdate(BaseModel):
    status: str


class MedicineResponse(BaseModel):
    id: int
    name: str
    medical_function: str
    price: str

    class Config:
        orm_mode=True


class OrderResponse(OrdersBase):
    medicines: List[MedicineResponse] = None


class Orders(OrdersBase):
    pass
