from typing import TypeVar, Generic
from sqlalchemy.orm import Session

from db.base import Base

ModelType = TypeVar("ModelType", bound=Base)

# This is a logic you can use to any services
class BaseService(Generic[ModelType]):  # get all "any" record from database
    def __init__(self, model):
        self.model = model

    def get_all(
        self, session: Session, skip: int = 0, limit: int = 100
    ):  # Get all data from a table
        return session.query(self.model).offset(skip).limit(limit).all()

    def get_one(self, session: Session, id: int):  # Get one row with ID
        return session.query(self.model).filter(self.model.id == id).first()

    def create_one(self, session: Session, obj: any):
        translate = self.model()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        session.add(translate)
        session.commit()
        session.refresh(translate)
        return translate

    def create_one_temp(self, session: Session, obj: any):
        translate = self.model()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        session.add(translate)
        return translate

    def save(self, session: Session, obj: ModelType):
        session.commit()
        session.refresh(obj)
        return obj


    def update(self, session: Session, id: int, data: any):
        instance = session.query(self.model).filter(self.model.id == id).first()

        if instance:
            for k in dict(data):
                setattr(instance, k, getattr(data, k, ""))
            session.add(instance)
            session.commit()
            session.refresh(instance)
        return instance

    def delete_one(self, session: Session, id: int):  # Delete one row using ID
        db_delete = session.query(self.model).filter(self.model.id == id).first()
        session.delete(db_delete)
        session.commit()
        session.close()
        return db_delete

    def authenticate(self, session: Session, user_name: str):
        authen_by_user_name = session.query(self.model).filter(self.model.user_name == user_name).first()
        if not authen_by_user_name:
            return None
        return authen_by_user_name
