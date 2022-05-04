from pydantic import BaseModel

#Những thông tin permissions có thể đọc
class PermissionsBase (BaseModel):
    title : str = None
    description : str = None


    class Config:
        orm_mode = True

#Create thêm permission
class PermissionsCreate (PermissionsBase):
    pass

#Update thêm permission
class PermissionsUpdate (PermissionsBase):
    pass

class Permissions (PermissionsBase):
    id : int