from datetime import date
from typing import Optional
from pydantic import BaseModel

#You can read data from these models
class UsersBase (BaseModel):
    id : int
    role_id : Optional[int] = None
    user_name: Optional[str] = None
    password: Optional[str] = None
    name : Optional[str] = None
    gender : Optional[int] = None
    date_of_birth : Optional[date] = None
    email : Optional[str] = None
    address : Optional[str] = None
    phone_numbers: Optional[str] = None

    class Config:
        orm_mode = True

#FastApi will using these models to create data
class UsersCreate (UsersBase):
    pass

#FastApi will using these models to update data
class UsersUpdate (UsersBase):
    pass

#Thừa kế từ UserBase, có thể truy xuất, thêm,sửa ,xóa những thông tin mà userbase có thông qua ID
class User (UsersBase):
    id : int