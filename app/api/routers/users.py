from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core import JWTBearer
from models import UsersBase, UsersCreate, UsersUpdate, User
from services import user_services
from db.engine import create_session

router = APIRouter()

# get all users from database
@router.get("/users", tags=["user"], response_model=list[User])
def read_users(
    skip: int = 0, limit: int = 200, session: Session = Depends(create_session)
):
    user = user_services.get_all(session, skip=skip, limit=limit)
    return user


# get 1 user from database
@router.get("/user/{id}", tags=["user"], response_model=UsersBase)
def read_user(id: int, session: Session = Depends(create_session)):
    user = user_services.get_one(session, id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found.")
    return user


# create a brand new user
@router.post("/user", tags=["user"], response_model=UsersBase)
def create_user(user_schemas: UsersCreate, session: Session = Depends(create_session)):
    user = user_services.check_user_name(
        session=session, user_name=user_schemas.user_name
    )
    if user:
        raise HTTPException(
            status_code=400, detail="User with this user_name already exist in database"
        )

    user = user_services.check_phone_number(
        session=session, phone=user_schemas.phone_numbers
    )
    if user:
        raise HTTPException(
            status_code=400,
            detail="User with this phone number already exist in database",
        )
    user = user_services.create_one(session, user_schemas)
    return user


# update some thing in a user
@router.put("/user/{id}", tags=["user"], response_model=UsersUpdate)
def update_user(
    id: int, user_schemas: UsersUpdate, session: Session = Depends(create_session)
):
    user = user_services.update(session, id=id, data=user_schemas)
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
