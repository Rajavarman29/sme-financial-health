from fastapi import FastAPI
from app.routes import auth, upload, metrics

app = FastAPI(title="SME Financial Health API")

app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(metrics.router)
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "SME Financial Health API is running"
    }
