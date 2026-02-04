import pandas as pd


def calculate_monthly_totals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Groups by month and sums amounts.
    """
    if df.empty:
        return pd.DataFrame(columns=["month", "total"])

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)

    return (
        df.groupby("month")["amount"]
        .sum()
        .reset_index(name="total")
    )


def calculate_net_cash_flow(revenue_df: pd.DataFrame, expense_df: pd.DataFrame) -> float:
    total_revenue = revenue_df["amount"].sum() if not revenue_df.empty else 0.0
    total_expenses = expense_df["amount"].sum() if not expense_df.empty else 0.0
    return total_revenue - total_expenses
