from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import PermissionsBase
from services import permission_services
from db.engine import create_session

router = APIRouter()

# get all permissions from database
@router.get("/Permissions", tags=["permission"], response_model=list[PermissionsBase])
def read_permissions(
    skip: int = 0, limit: int = 200, session: Session = Depends(create_session)
):
    permission = permission_services.get_all(session, skip=skip, limit=limit)
    return permission


# get 1 permission from database
@router.get("/Permission/{id}", tags=["permission"], response_model=PermissionsBase)
def read_permission(id: int, session: Session = Depends(create_session)):
    permission = permission_services.get_one(session, id)
    if not permission:
        raise HTTPException(
            status_code=404, detail=f"Permission with ID {id} not found"
        )
    return permission
