from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from models import RolesBase, Roles
from services import role_services
from db.engine import create_session

router = APIRouter()

# get all roles from database
@router.get("/roles", tags=["role"], response_model=list[RolesBase])
def read_roles(
    skip: int = 0, limit: int = 200, session: Session = Depends(create_session)
):
    role = role_services.get_all(session, skip=skip, limit=limit)
    if not role:
        raise HTTPException(
            status_code=404, detail="We don't have the results you're looking for."
        )
    return role


# get 1 role from database
@router.get("/role/{id}", tags=["role"], response_model=RolesBase)
def read_roles(id: int, session: Session = Depends(create_session)):
    role = role_services.get_one(session, id)
    if not role:
        raise HTTPException(
            status_code=404, detail=f"Role with ID {id} not found."
        )
    return role

