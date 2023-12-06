# Home Assignment for Tuesday (8th Aug): Develop a Python program that efficiently organizes and analyzes sales data to provide actionable insights for a small business owner.
# 	The business owner has sales data scattered across various files and folders, containing vital details like product information, quantities sold, prices, and sale dates.  To make informed decisions, the owner seeks a solution to streamline data organization and obtain key sales metrics.
# 	Requirements:
# 	1. Directory Organization: Create specialized subdirectories (invoices, reports) within a primary directory to categorize sales data files.
# 	2. Data Extraction: Extract essential details (product names, quantities, prices, dates) from sales data files.
# 	3. Sales Metrics: Calculate and present fundamental metrics, including total sales revenue within a specified period, average sale price, and the most popular product by quantities.
# 	4. Summary Report: Generate a concise report summarizing key insights such as total sales count, highest/lowest selling products, and overall revenue

import os
from datetime import datetime 
import csv

# 1. Primary_directory is sales_data -> Its sub-directories are invoice and reports
primary_directory = "sales_data"
sub_directories = ["invoice", "reports"]
for sub_dir in sub_directories:
    os.makedirs(os.path.join(primary_directory, sub_dir), exist_ok=True)

# Function to extract data
# 2. Data Extraction: Extract essential details (product names, quantities, prices, dates) from sales data files.
def extract_data(filepath):
    try:
        data=[]
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
            return data

    except Exception as e:
        print("There was error while extracting information: ", e)
        return None

# Sales Metrics: Calculate and present fundamental metrics, including total sales revenue within a specified period, average sale price, and the most popular product by quantities.

def calculate_sales_metrics(data):
    if data is None:
        return None
    
    total_sales_revenue = 0
    total_quantity = 0
    product_quantities = {}

    for row in data:
        quantity = int(row["quantity"])
        price = int(row["price"])
        total_sales_revenue += quantity*price
        total_quantity += 1

        product_name = row["product_name"]
        if product_name in product_quantities:
            product_quantities[product_name] += quantity
        else:
            product_quantities[product_name] = quantity


    average_sales_revenue = total_sales_revenue/total_quantity
    most_popular_product = max(product_quantities, key=product_quantities.get)
    return average_sales_revenue, most_popular_product, total_quantity

# 4. Summary Report: Generate a concise report summarizing key insights such as total sales count, highest/lowest selling products, and overall revenue

def summary_report_generation(average_sales_revenue, most_popular_product, total_quantity):
    summary_report = f"Sales Summary Report: \n"
    summary_report += f"Total Sales Count: {total_quantity}\n"
    summary_report += f"Most Popular Product: {most_popular_product}\n"
    summary_report += f"Average Sales Revenue: {average_sales_revenue:.2f}\n"
    return summary_report

# Main Function
def main():
    sales_files = [f for f in os.listdir(os.path.join(primary_directory, "invoice")) if f.endswith(".csv")]

    total_sales_count = 0
    highest_selling_product = ""
    total_revenue = 0

    total_quantity = 0
    total_sales_revenue = 0
    most_popular_product = ""
    average_sales_revenue = 0

    for file in sales_files:
        file_path = os.path.join(primary_directory, "invoice", file)
        data = extract_data(file_path)
        if data is not None:
            metrics = calculate_sales_metrics(data)
            if metrics is not None:
                avg_revenue, most_popular, quantity = metrics
                total_quantity += quantity
                total_sales_count += len(data)
                total_sales_revenue += avg_revenue * quantity
                most_popular_product = most_popular
                average_sales_revenue = avg_revenue

    if total_quantity > 0:
        total_revenue = total_sales_revenue

    report = summary_report_generation(average_sales_revenue, most_popular_product, total_quantity)
    # print(report)
    report_file_path = os.path.join(primary_directory, "reports", "summary.txt")
    with open(report_file_path, "w") as report_file:
        report_file.write(report)

if __name__ == "__main__":
    main()
