from fastapi import APIRouter, Depends, status, HTTPException
# сессия базы данных
from sqlalchemy.orm import Session
# функция подключения к базе данных
from backend.db_depends import get_db
# аннотации, модели БД и  Pydantic
from typing import Annotated
from models.task import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    get_all_tasks = db.scalars(select(Task)).all()
    return get_all_tasks



@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    raise HTTPException()


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is not None:
        db.execute(insert(Task).values(title = create_task.title,
                                      content = create_task.content,
                                      user_id = user_id,
                                      slug= slugify(create_task.title)))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Пользователь успешно обновлён!'
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db.scalars(select(Task).where(Task.id == task_id))

    if task is not None:
        db.execute(update(Task).where(Task.id == task_id).values(title = update_task.title,
                                                                 content = update_task.content,
                                                                 slug= slugify(update_task.title),
                                                                 priority =update_task.priority))
        db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Пользователь успешно обновлён!'
            }
    raise HTTPException(status_code=404, detail='User not found')


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    delete_task = db.scalars(select(Task).where(Task.id == task_id))

    if delete_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
