from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import user, transaction  # noqa: F401 - imported for side effects (model registration)
from app.routes import auth, upload, metrics

app = FastAPI(title="SME Financial Health API")

# Ensure database tables are created (for demo / Render deployment)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(metrics.router)
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "SME Financial Health API is running"
    }
