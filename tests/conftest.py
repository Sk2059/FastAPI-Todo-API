
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import Base, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)