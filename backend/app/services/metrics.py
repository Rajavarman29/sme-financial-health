import pandas as pd
from sqlalchemy.orm import Session

from app.services.data_loader import load_revenues, load_expenses


def get_financial_metrics(db: Session, user_id: str):
    # Load decrypted revenues and expenses for the user
    revenues_df = load_revenues(db, user_id)
    expenses_df = load_expenses(db, user_id)

    # If there is no data at all, return empty structures
    if revenues_df.empty and expenses_df.empty:
        return {
            "monthly_revenue": [],
            "monthly_expenses": [],
            "net_cash_flow": []
        }

    # Ensure date column is datetime and month is derived
    if not revenues_df.empty:
        revenues_df["date"] = pd.to_datetime(revenues_df["date"])
        revenues_df["month"] = revenues_df["date"].dt.to_period("M").astype(str)
    if not expenses_df.empty:
        expenses_df["date"] = pd.to_datetime(expenses_df["date"])
        expenses_df["month"] = expenses_df["date"].dt.to_period("M").astype(str)

    # Monthly Revenue
    if not revenues_df.empty:
        monthly_revenue = (
            revenues_df.groupby("month")["amount"]
            .sum()
            .reset_index()
            .rename(columns={"amount": "total_revenue"})
        )
    else:
        monthly_revenue = pd.DataFrame(columns=["month", "total_revenue"])

    # Monthly Expenses
    if not expenses_df.empty:
        monthly_expenses = (
            expenses_df.groupby("month")["amount"]
            .sum()
            .reset_index()
            .rename(columns={"amount": "total_expenses"})
        )
    else:
        monthly_expenses = pd.DataFrame(columns=["month", "total_expenses"])

    # Net Cash Flow
    net_cash_flow = pd.merge(
        monthly_revenue,
        monthly_expenses,
        on="month",
        how="outer"
    ).fillna(0)

    if not net_cash_flow.empty:
        net_cash_flow["net_cash_flow"] = (
            net_cash_flow["total_revenue"]
            - net_cash_flow["total_expenses"]
        )

    return {
        "monthly_revenue": monthly_revenue.to_dict(orient="records"),
        "monthly_expenses": monthly_expenses.to_dict(orient="records"),
        "net_cash_flow": net_cash_flow.to_dict(orient="records")
    }
