from sqlalchemy import Integer, String, Column

from db.base import Base

# Create database "tbl_permissions"
class Permissions(Base):
    __tablename__ = "tbl_permissions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
