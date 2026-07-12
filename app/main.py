from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.api.router.user import router as user_router

app = FastAPI()

app.include_router(user_router)