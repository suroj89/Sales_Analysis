import matplotlib.pyplot as plt
import os

def create_output_folder():
    os.makedirs("outputs", exist_ok=True)


def plot_monthly_sales(data):
    if data is None:
        return
    data.plot(kind="bar")
    plt.title("Monthly Sales")
    plt.tight_layout()
    plt.savefig("outputs/monthly_sales.png")
    plt.close()


def plot_category_sales(data):
    if data is None:
        return
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/category_sales.png")
    plt.close()