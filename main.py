from src.data_loader import load_data
from src.analysis import (
    total_sales,
    total_profit,
    monthly_sales,
    category_sales
)
from src.visualization import (
    create_output_folder,
    plot_monthly_sales,
    plot_category_sales
)

def main():
    file_path = "data\ecommerce_sales_data.csv"   # 🔁 replace CSV only

    df = load_data(file_path)
    create_output_folder()

    total = total_sales(df)
    profit = total_profit(df)
    monthly = monthly_sales(df)
    category = category_sales(df)

    plot_monthly_sales(monthly)
    plot_category_sales(category)

    with open("outputs/summary_report.txt", "w") as f:
        f.write(f"Total Sales: {total}\n")
        f.write(f"Total Profit: {profit}\n")

    print("✅ Analysis completed. Check outputs folder.")

if __name__ == "__main__":
    main()