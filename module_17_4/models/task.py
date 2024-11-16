from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean# ForeignKey позволяет указать на другую ячейку и произвести связь между таблицами
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from models import *
# from models.user import User

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    complited = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True) # обращение к ключу по имени таблицы!
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates= 'tasks')

CreateTaskTable = CreateTable(Task.__table__)

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))


# from app.backend.db import Base
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
# 
# 
# class Task(Base):
#     __tablename__ = 'tasks'
#     __table_args__ = {'extend_existing': True}
# 
#     id = Column(Integer, primary_key=True, index=True)
# 
#     title = Column(String)
#     content = Column(String)
#     priority = Column(Integer, default=0)
#     completed = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)
# 
#     slug = Column(String, unique=True, index=True)
# 
#     user = relationship('User', back_populates='tasks')


# from app.backend.db import Base
# from sqlalchemy import Column, ForeignKey, Integer, String, Boolean# ForeignKey позволяет указать на другую ячейку и произвести связь между таблицами
# from sqlalchemy.orm import relationship
# from app.models import *
#
# class Task(Base):
#     __tablename__ = 'tasks'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     content = Column(String)
#     priority = Column(Integer, default=0)
#     complited = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey('tasks.id'), nullable=False, index=True)
#     slug = Column(String, unique=True, index=True)
#
#     user = relationship('User', back_populates= 'tasks')
#
# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))