import pandas as pd

# ---------- UNIVERSAL COLUMN FINDER ----------
def find_column(df, keywords):
    for col in df.columns:
        for key in keywords:
            if key in col:
                return col
    return None


# ---------- ANALYSIS FUNCTIONS ----------
def total_sales(df):
    sales_col = find_column(df, ["sales", "revenue", "amount"])
    return df[sales_col].sum()


def total_profit(df):
    profit_col = find_column(df, ["profit", "margin"])
    return df[profit_col].sum() if profit_col else "Not Available"


def monthly_sales(df):
    date_col = find_column(df, ["date", "order"])
    sales_col = find_column(df, ["sales", "revenue", "amount"])

    if not date_col:
        return None

    df[date_col] = pd.to_datetime(df[date_col])
    df["month"] = df[date_col].dt.to_period("M")
    return df.groupby("month")[sales_col].sum()


def category_sales(df):
    category_col = find_column(df, ["region", "category", "store", "product", "item"])
    sales_col = find_column(df, ["sales", "revenue", "amount"])

    if not category_col:
        return None

    return df.groupby(category_col)[sales_col].sum()