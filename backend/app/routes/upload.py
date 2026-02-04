from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from app.core.database import get_db
from app.core.security import encrypt_value
from app.models.transaction import Revenue, Expense

router = APIRouter(prefix="/upload", tags=["upload"])

REQUIRED_COLUMNS = {"date", "amount", "type", "category"}

@router.post("/")
async def upload_file(
    user_id: str,
    file: UploadFile,
    db: Session = Depends(get_db)
):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file format")

    df = pd.read_csv(file.file) if file.filename.endswith(".csv") else pd.read_excel(file.file)

    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise HTTPException(status_code=400, detail="Missing required columns")

    for _, row in df.iterrows():
        if row["type"] == "revenue":
            record = Revenue(
                user_id=user_id,
                date=row["date"],
                amount=encrypt_value(str(row["amount"])),
                category=encrypt_value(row["category"])
            )
        elif row["type"] == "expense":
            record = Expense(
                user_id=user_id,
                date=row["date"],
                amount=encrypt_value(str(row["amount"])),
                category=encrypt_value(row["category"])
            )
        else:
            continue

        db.add(record)

    db.commit()
    return {"message": "File processed successfully"}
