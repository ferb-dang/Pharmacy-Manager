from sqlalchemy import  Column, ForeignKey, Table


from db.base import Base

# Create association database  connect "tbl_roles" with "tbl_permissions"
role_permission = Table(
    "tbl_role_permissions",
    Base.metadata,
    Column("roles_id", ForeignKey("tbl_roles.id"), primary_key=True),
    Column("permissions_id", ForeignKey("tbl_permissions.id"), primary_key=True),
)
