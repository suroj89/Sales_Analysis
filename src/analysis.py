def total_sales(df):
    return df["Sales"].sum()

def monthly_sales(df):
    df["Month"]=df["Date"].dt.to_period("M")
    return df.groupby("Month")["Sales"].sum()

def region_sales(df):
    return df.groupby("Region")["Sales"].sum()

def top_product(df):
    return df.groupby("Product")["Sales"].sum()

def total_profit(df):
    return df["Profit"].sum()

