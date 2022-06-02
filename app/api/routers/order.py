from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from models import OrdersBase, OrdersUpdate, OrdersCreate, OrderResponse, Orders
from services import order_services
from db.engine import create_session
from core.security import JWTBearer, decode_jwt

router = APIRouter()

# get all orders from database
@router.get(
    "/orders",
    tags=["order"],
    response_model=list[OrderResponse],
    dependencies=[Depends(JWTBearer([1]))],
)
def read_orders(skip: int = 0, limit: int = 200, session: Session = Depends(create_session)):

    orders = order_services.get_all(session, skip=skip, limit=limit)
    if not orders:
        raise HTTPException(
            status_code=404, detail="We don't have the results you're looking for."
        )
    return orders


# get 1 order from database
@router.get(
    "/order/{id}",
    tags=["order"],
    response_model=OrderResponse,
    dependencies=[Depends(JWTBearer([1, 2, 3, 4]))],
)
def read_order(id: int, session: Session = Depends(create_session)):
    order = order_services.get_one(session, id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {id} not found.")
    return order


# create 1 order
@router.post(
    "/order",
    tags=["order"],
    response_model=OrderResponse,
)
def create_order(
    order_schemas: OrdersCreate,
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer([1, 2, 3, 4])),
    session: Session = Depends(create_session),
):
    payload = decode_jwt(credentials)
    user_id = payload.get("sub", {}).get("user_id", {})
    order = order_services.create_one(session, order_schemas, user_id)
    return order


# update some thing in a order
@router.put(
    "/order/{id}",
    tags=["order"],
    response_model=OrdersUpdate,
    dependencies=[Depends(JWTBearer([1, 2, 3]))],
)
def update_order(
    id: int, order_schemas: OrdersUpdate, session: Session = Depends(create_session)
):
    order = order_services.update(session, id=id, data=order_schemas)
    if not order:
        raise HTTPException(status_code=400, detail=" ID not exist in database!")

    return order


# delete a order with ID
@router.delete(
    "/order/{id}", tags=["order"], dependencies=[Depends(JWTBearer([1, 2, 3]))]
)
def delete_order(id: int, session: Session = Depends(create_session)):
    order = order_services.get_one(session, id)
    session.close()
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id {id} not found")

    return f"Succesfully delete order with id: {id}"
