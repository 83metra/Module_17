from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean# ForeignKey позволяет указать на другую ячейку и произвести связь между таблицами
from sqlalchemy.orm import relationship
from models import *
# import app.models
# from .task import Task # не нужно, если в alembic.ini прописан импорт from app.models.task import Task


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} #!
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable
CreateUserTable = CreateTable(User.__table__)
print(CreateUserTable)



# from app.backend.db import Base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from sqlalchemy.schema import CreateTable
# from task import Task
#
# class User(Base):
#     __tablename__ = 'users'
#     __table_args__ = {'extend_existing': True}
#
#     id = Column(Integer, primary_key=True, index=True)
#
#     username = Column(String)
#     firstname = Column(String)
#     lastname = Column(String)
#     age = Column(Integer)
#
#     slug = Column(String, unique=True, index=True)
#
#     tasks = relationship('Task', back_populates='user', cascade='save-update, merge, delete')
#
# print(CreateTable(User.__table__))
# print(CreateTable(Task.__table__))






# from app.backend.db import Base
# from sqlalchemy import Column, ForeignKey, Integer, String, Boolean# ForeignKey позволяет указать на другую ячейку и произвести связь между таблицами
# from sqlalchemy.orm import relationship
# from app.models import *
# import app.models
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String)
#     firsname = Column(String)
#     lastname = Column(String)
#     age = Column(Integer)
#     slug = Column(String, unique=True, index=True)
#
#     tasks = relationship('Task', back_populates='users')
#
# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))

