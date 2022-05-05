from dbmodels import Orders
from .base import BaseService


class OrderService(BaseService[Orders]):
    pass

order_services = OrderService(Orders) #get_one and get_all and delete_one

