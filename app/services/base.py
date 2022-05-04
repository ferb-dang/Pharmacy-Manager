from typing import TypeVar, Generic
from sqlalchemy.orm import Session

from db.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[ModelType]):  # get all "any" record from database

    def __init__(self, model):
        self.model = model

    def get_all(self, session: Session, skip: int = 0, limit: int = 100):
        return session.query(self.model).offset(skip).limit(limit).all()

    def get_one(self, session: Session, id: int):
        return session.query(self.model).filter(self.model.id == id).first()

    # def create(self, session: Session, obj: any) -> ModelType:
    #     instance = self.model()
    #     return map(lambda item: setattr(instance, *item), dict(obj).items())

    def create(self, obj: any):
        translate = self()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        return translate

    # def save(self,session: Session, obj: ModelType):
    #     session.add(obj)
    #     session.save
