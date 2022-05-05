from pydantic import BaseModel


#You can read data from these models
class OrdersBase (BaseModel):
    status : str = None
    shipping_address : str = None
    shipping_fee : str = None

    class Config:
        orm_mode = True

#FastApi will using these models to create data
class OrdersCreate (OrdersBase):
    pass

#FastApi will using these models to update order fee and address
class OrdersUpdate (OrdersBase):
    shipping_address : str
    shipping_fee : str

#FastApi will using these models to update status
class OrdersStatusUpdate (OrdersBase):
    status : str

class Orders (OrdersBase):
    id : int