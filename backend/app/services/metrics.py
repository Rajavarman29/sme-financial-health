from sqlalchemy.orm import Session
from uuid import UUID
from app.models import Revenue, Expense


def get_financial_metrics(db: Session, user_id: str):


    
    try:
        user_uuid = UUID(user_id)
    except ValueError:
        raise ValueError("Invalid user_id format")

    
    revenues = db.query(Revenue).filter(Revenue.user_id == user_uuid).all()
    expenses = db.query(Expense).filter(Expense.user_id == user_uuid).all()

    
    monthly_revenue = sum(r.amount for r in revenues)
    monthly_expenses = sum(e.amount for e in expenses)

    net_cashflow = monthly_revenue - monthly_expenses

    return {
        "monthly_revenue": float(monthly_revenue),
        "monthly_expenses": float(monthly_expenses),
        "net_cashflow": float(net_cashflow),
    }
