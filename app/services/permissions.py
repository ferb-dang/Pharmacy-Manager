from dbmodels import Permissions
from .base import BaseService


class PermissionService(BaseService[Permissions]):
    pass


permission_services = PermissionService(
    Permissions
)  # get_one and get_all and delete_one
