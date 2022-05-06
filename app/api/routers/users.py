from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import UsersBase,UsersCreate,UsersUpdate
from services import user_services, get_by_phone_number
from db.engine import create_session

router = APIRouter()

# get all users from database
@router.get("/users", tags=["user"], response_model=list[UsersBase])
def read_users(
    skip: int = 0, limit: int = 200, session: Session = Depends(create_session)
):
    user = user_services.get_all(session, skip=skip, limit=limit)
    return user


# get 1 user from database
@router.get("/user/{id}", tags=["user"], response_model=UsersBase)
def read_user(id: int, session: Session = Depends(create_session)):
    user = user_services.get_one(session, id)
    return user


# create a brand new user
@router.post("/user", tags=["user"], response_model=UsersCreate)
def create_user(
    user_schemas: UsersCreate, session: Session = Depends(create_session)
):
    user = get_by_phone_number(session, phone=user_schemas.phone_numbers)
    if user:
        raise HTTPException(status_code=400, detail="User with this ID already exist in database")

    user = user_services.create_one(session, user_schemas)
    return user


# update some thing in a user
@router.put("/user/{id}", tags=["user"], response_model=UsersUpdate)
def update_user(
    id: int,
    user_schemas: UsersUpdate,
    session: Session = Depends(create_session)
):
    user = user_services.update(session, id = id, data=user_schemas)
    if not user:
        raise HTTPException(status_code=400, detail="ID not exist in database!")

    return user 

# delete a user with ID
@router.delete("/user/{id}", tags=["user"])
def delete_user(id: int, session: Session = Depends(create_session)):
    user = user_services.get_one(session, id)
    session.close()
    if not user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found")

    return f"Succesfully delete user with id: {id}"