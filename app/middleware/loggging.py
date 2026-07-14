from datetime import datetime
import time
from urllib import response
from fastapi import Request

async def logging_middleware(request:Request,call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time()-start_time

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"Status:{response.status_code} "
        f"Time:{process_time:.4f}s"
    )

    response.headers["X-Process-Time"]=str(process_time)

    return response