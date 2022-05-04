from pydantic import BaseModel


#Những thông tin được đọc về Order
class OrdersBase (BaseModel):
    status : str = None
    shipping_address : str = None
    shipping_fee : str = None

    class Config:
        orm_mode = True

#Những thông tin Order được tạo ra
class OrdersCreate (OrdersBase):
    shipping_address : str
    shipping_fee : str

#Update trạng thái của order
class OrdersStatusUpdate (OrdersBase):
    status : str

#Update thông tin về địa chỉ vận chuyển và chi phí
class OrdersStatusUpdate (OrdersBase):
    shipping_address : str
    shipping_fee : str

class Orders (OrdersBase):
    id : int