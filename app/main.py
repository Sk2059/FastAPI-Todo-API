from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.api.router.user import router as user_router
from app.api.router.task import router as task_router
from app.middleware.loggging import logging_middleware

from app.core.database import engine
from app.core.database import Base
Base.metadata.create_all(bind=engine)

from app.exceptions.costom_exceptions import (
    TaskNotFoundException,
    UserNotFoundException,
    InvalidCredentialsException,
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException
)

from app.exceptions.handlers import (
    task_not_found_handler,
    user_not_found_handler,
    invalid_credentials_handler,
    email_exists_handler,
    username_exists_handler
)
app = FastAPI()

app.middleware("http")(logging_middleware)

app.include_router(user_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "my fastapi application is running"}

app.add_exception_handler(
    TaskNotFoundException,
    task_not_found_handler
)
app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler
)

app.add_exception_handler(
    EmailAlreadyExistsException,
    email_exists_handler
)

app.add_exception_handler(
    UsernameAlreadyExistsException,
    username_exists_handler
)