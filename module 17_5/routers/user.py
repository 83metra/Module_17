from fastapi import APIRouter, Depends, status, HTTPException
# сессия базы данных
from sqlalchemy.orm import Session
# функция подключения к базе данных
from backend.db_depends import get_db
# аннотации, модели БД и  Pydantic
from typing import Annotated
from models.user import User
from models.task import Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify  # python-slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    get_all_users = db.scalars(select(User)).all()
    return get_all_users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    get_user = db.scalars(select(User).where(User.id == user_id)).first()
    if get_user is not None:
        return get_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Пользователь не найден'
    )


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(
        insert(User).values(username=create_user.username,
                            firstname=create_user.firstname,
                            lastname=create_user.lastname,
                            age=create_user.age,
                            slug=slugify(create_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Пользователь успешно создан!'
    }


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = db.scalars(select(User).where(User.id == user_id)).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Пользователь не найден')

    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Пользователь успешно обновлён!'
    }


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()

    if user is not None:
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Пользователь успешно удалён!'
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Пользователь не найден'
    )


@router.get('/user_id/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id):
    tasks = list(db.scalars(select(Task).where(Task.user_id == user_id)))
    return tasks
