from pydantic import BaseModel

#You can read data from these models
class RolesBase (BaseModel):
    title: str = None
    description: str = None


    class Config:
        orm_mode = True

#FastApi will using these models to create data
class RolesCreate (RolesBase):
    pass


#FastApi will using these models to update data
class RolesUpdate (RolesBase):
    pass


class Roles (RolesBase):
    id: int
