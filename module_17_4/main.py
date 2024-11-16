from fastapi import FastAPI
from routers import task, user
# import sqlite3
# from models.user import CreateUserTable
# from models.task import CreateTaskTable

app = FastAPI()

# connection = sqlite3.connect('taskmanager.db')
# cursor = connection.cursor()
# def create_user_table():
#
#     cursor.execute(f'{CreateUserTable}')
#     cursor.execute(f'{CreateTaskTable}')
#     cursor.close()
#
# create_user_table()


# pip install alembic
# alembic init migrations
# alembic upgrade head

@app.get('/')
async def welcome():
    return {'message': 'Welcome to TaskManager'}

app.include_router(task.router)
app.include_router(user.router)