from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.api.router.user import router as user_router
from app.api.router.task import router as task_router

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)