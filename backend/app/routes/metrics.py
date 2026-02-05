from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.metrics import get_financial_metrics

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/")
def metrics(user_id: str, db: Session = Depends(get_db)):
    return get_financial_metrics(db, user_id)
