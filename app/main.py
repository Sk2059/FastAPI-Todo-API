from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message":"my fastapi application is running"}