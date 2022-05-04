from pydantic import BaseModel

# Những thông tin roles có thể đọc


class RolesBase (BaseModel):
    title: str = None
    description: str = None
    slug: str = None

    class Config:
        orm_mode = True

# Create thêm permission


class RolesCreate (RolesBase):
    pass

# Update thêm permission


class RolesUpdate (RolesBase):
    pass


class Roles (RolesBase):
    id: int
