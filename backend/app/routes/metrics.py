from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.data_loader import load_revenues, load_expenses
from app.services.metrics import calculate_monthly_totals, calculate_net_cash_flow

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/")
def get_metrics(user_id: str, db: Session = Depends(get_db)):
    revenues_df = load_revenues(db, user_id)
    expenses_df = load_expenses(db, user_id)

    monthly_revenue = calculate_monthly_totals(revenues_df)
    monthly_expenses = calculate_monthly_totals(expenses_df)
    net_cash_flow = calculate_net_cash_flow(revenues_df, expenses_df)

    return {
        "monthly_revenue": monthly_revenue.to_dict(orient="records"),
        "monthly_expenses": monthly_expenses.to_dict(orient="records"),
        "net_cash_flow": net_cash_flow
    }
