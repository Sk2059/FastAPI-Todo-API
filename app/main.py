from fastapi import FastAPI
from app.core.database import engine
from sqlalchemy import text
print("engine",engine)
app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message":"my fastapi application is running"}

from sqlalchemy import text

@app.get("/health")
def health_check():
    print("1. Route entered")

    try:
        print("2. Attempting database connection")

        with engine.connect() as connection:
            print("3. Database connected")

            result = connection.execute(text("SELECT 1"))

            print("4. Query executed")

            return {
                "database": "connected",
                "result": result.scalar()
            }

    except Exception as e:
        print("ERROR:", repr(e))
        return {"error": str(e)}