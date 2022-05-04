from datetime import date
from lib2to3.pytree import Base
from pydantic import BaseModel

#Những thông tin được đọc từ users
class UsersBase (BaseModel):
    role_id : int = None
    name : str = None
    gender : int = None
    date_of_birth : date = None
    email : str = None
    address : str = None 
    phone_numbers: str = None

    class Config:
        orm_mode = True

class UsersCreate (UsersBase):
    pass

class UsersUpdate (UsersBase):
    pass

#Thừa kế từ UserBase, có thể truy xuất, thêm,sửa ,xóa những thông tin mà userbase có thông qua ID
class User (UsersBase):
    id : int