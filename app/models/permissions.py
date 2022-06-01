from pydantic import BaseModel

# You can read data from these models
class PermissionsBase(BaseModel):
    title: str = None
    description: str = None

    class Config:
        orm_mode = True


# FastApi will using these models to create data
class PermissionsCreate(PermissionsBase):
    pass


# FastApi will using these models to update data
class PermissionsUpdate(PermissionsBase):
    pass


class Permissions(PermissionsBase):
    id: int
