from pydantic import BaseModel
from typing import Optional


#You can read data from these models
class OrdersBase (BaseModel):
    status : Optional[str] = None
    shipping_address : Optional[str] = None
    shipping_fee : Optional[str] = None

    class Config:
        orm_mode = True

#FastApi will using these models to create data
class OrdersCreate (OrdersBase):
    pass

#FastApi will using these models to update order fee and address
class OrdersUpdate (OrdersBase):
    pass

#FastApi will using these models to update status
class OrdersStatusUpdate (BaseModel):
    status : str

class Orders (OrdersBase):
    id : int