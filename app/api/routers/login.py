from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from core import sign_jwt, password_hash
from models import UserSignIn, UserLogin
from dbmodels import Users
from db.engine import create_session
from services import user_services

router = APIRouter()


@router.post("/signup", tags=["login"])
def signup_user(user_schemas: UserSignIn, session: Session = Depends(create_session)):
    user = user_services.check_user_name(
        session=session, user_name=user_schemas.user_name
    )
    if user:
        raise HTTPException(status_code=400, detail="This user name is taken")

    user = user_services.create_user(session, user_schemas)
    return sign_jwt(
        {"user_name": user.user_name, "user_id": user.id, "role": user.role_id}
    )


@router.post("/login", tags=["login"])
def user_login(user_schemas: UserLogin, session: Session = Depends(create_session)):
    hashed_password = password_hash(user_schemas.password)
    user = user_services.check_exist_user(
        session=session, user_name=user_schemas.user_name, password=hashed_password
    )
    if user:
        return sign_jwt(
            {"user_name": user.user_name, "user_id": user.id, "role": user.role_id}
        )
    raise HTTPException(status_code=400, detail="Invalid login detail!")
