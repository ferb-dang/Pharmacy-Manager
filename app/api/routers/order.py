from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import  OrdersBase, OrdersUpdate
from services import order_services
from db.engine import create_session

router = APIRouter()

# get all orders from database
@router.get("/orders", tags=["order"], response_model=list[OrdersBase])
def read_orders(
    skip: int = 0, limit: int = 200, session: Session = Depends(create_session)
):
    order = order_services.get_all(session, skip=skip, limit=limit)
    return order


# get 1 order from database
@router.get("/order/{id}", tags=["order"], response_model=OrdersBase)
def read_order(id: int, session: Session = Depends(create_session)):
    order = order_services.get_one(session, id)
    return order

# update some thing in a order
@router.put("/order/{id}",tags=["order"], response_model=OrdersUpdate)
def update_order(
    id: int,
    order_schemas: OrdersUpdate,
    session: Session = Depends(create_session)
):
    order = order_services.update(session, id = id, data=order_schemas)
    if not order:
        raise HTTPException(status_code=400, detail=" ID not exist in database!")

    return order 

# delete a order with ID
@router.delete("/order/{id}",tags=["order"])
def delete_order(id: int, session: Session = Depends(create_session)):
    order = order_services.get_one(session, id)
    session.close()
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id {id} not found")

    return f"Succesfully delete order with id: {id}"
