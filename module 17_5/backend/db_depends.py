from backend.db import SessionLockal

async def get_db():
    db = SessionLockal()
    try:
        yield db
    finally:
        db.close
        
# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


