from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.costom_exceptions import (
    TaskNotFoundException,
    UserNotFoundException,
    InvalidCredentialsException,
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException
)

async def task_not_found_handler(
        request:Request,
        exc:TaskNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success":False,
            "message":exc.message
        }
    )

async def user_not_found_handler(
        request:Request,
        exc:UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success":False,
            "message":exc.message
        }
    )

async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException
):
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": exc.message
        }
    )

async def email_exists_handler(
    request: Request,
    exc: EmailAlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message
        }
    )

async def username_exists_handler(
    request: Request,
    exc: UsernameAlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message
        }
    )

