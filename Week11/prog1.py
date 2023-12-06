import numpy as np
sales_data = np.array([[500,600,750,900], [300,350,400,450], [200,250,300,350]])
price_per_unit = np.array([10,15,20,25])
quaterly_revenue = np.dot(sales_data, price_per_unit)
print(quaterly_revenue)
print("Quaterly revenue for each category")
for i, revenue in enumerate(quaterly_revenue):
    print(f"Category {i+1}: Rs. {revenue}")