import matplotlib.pyplot as plt
import os

def create_output_folder():
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

def plot_monthly_sales(monthly_data):
    monthly_data.plot(kind="bar")
    plt.title("Monthly sales")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("outputs/monthly_sales.png")
    plt.close()

def plot_region_sales(region_date):
    region_date.plot(kind="pie",autopct="%1.1f%%")
    plt.title("Region sales Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/Region_sales.png")
    plt.close()