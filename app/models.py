from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(400), index=True)
    completed = Column(Boolean, default=False)