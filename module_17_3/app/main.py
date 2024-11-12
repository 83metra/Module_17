from fastapi import FastAPI
from routers import task, user

app = FastAPI()

# pip install alembic
# alembic init app/migrations

@app.get('/')
async def welcome():
    return {'message': 'Welcome to TaskManager'}

app.include_router(task.router)
app.include_router(user.router)