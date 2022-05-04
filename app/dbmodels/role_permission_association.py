from sqlalchemy import  Column, ForeignKey, Table


from db.base import Base

# Bảng csdl trung gian giữa Roles và Permissions
role_permission = Table(
    "tbl_role_permissions",
    Base.metadata,
    Column("permissions_id", ForeignKey("tbl_permissions.id"), primary_key=True),
    Column("roles_id", ForeignKey("tbl_roles.id"), primary_key=True),
)
