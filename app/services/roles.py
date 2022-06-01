from dbmodels import Roles
from .base import BaseService


class RoleService(BaseService[Roles]):
    pass


role_services = RoleService(Roles)  # get_one and get_all and delete_one
