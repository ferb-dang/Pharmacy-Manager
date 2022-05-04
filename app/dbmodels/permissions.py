from sqlalchemy import Integer, String, Column


from db.base import Base

class Permissions(Base):
    __tablename__ = "tbl_permissions"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    @classmethod
    def create(cls, obj: any):
        translate = cls()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        return translate