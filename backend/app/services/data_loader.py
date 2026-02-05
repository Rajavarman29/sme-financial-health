import uuid

import pandas as pd
from sqlalchemy.orm import Session

from app.models.transaction import Revenue, Expense
from app.core.security import decrypt_value


def _to_uuid(user_id: str) -> uuid.UUID:
    """
    Ensure the string user_id is treated as a proper UUID for queries.
    """
    return uuid.UUID(user_id)


def load_revenues(db: Session, user_id: str) -> pd.DataFrame:
    records = db.query(Revenue).filter(Revenue.user_id == _to_uuid(user_id)).all()

    data = [{
        "date": r.date,
        "amount": float(decrypt_value(r.amount)),
        "category": decrypt_value(r.category)
    } for r in records]

    return pd.DataFrame(data)


def load_expenses(db: Session, user_id: str) -> pd.DataFrame:
    records = db.query(Expense).filter(Expense.user_id == _to_uuid(user_id)).all()

    data = [{
        "date": e.date,
        "amount": float(decrypt_value(e.amount)),
        "category": decrypt_value(e.category)
    } for e in records]

    return pd.DataFrame(data)
