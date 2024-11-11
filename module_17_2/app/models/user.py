from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean# ForeignKey позволяет указать на другую ячейку и произвести связь между таблицами
from sqlalchemy.orm import relationship
from app.models import *
import app.models

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firsname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))