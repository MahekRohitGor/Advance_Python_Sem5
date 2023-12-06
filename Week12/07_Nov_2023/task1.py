import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df_numpy = pd.read_csv("Food_Preference.csv", header=None)
print(df_numpy)
last_row = df_numpy.iloc[-1].values
print(last_row)
csv = pd.read_csv("Food_Preference.csv")
print(csv.head(2))
print(csv.isnull().sum())
mean = csv["Age"].mean()
median = csv["Age"].median()
print(f"Mean of Age is: {mean}")
print(f"Median of Age is: {median}")

plt.figure(figsize=(8, 6))
plt.hist(csv['Gender'].astype(str), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

data = pd.read_csv('Food_Preference.csv')
data = data.dropna()

sns.barplot(x='Food', y='Nationality', data=data)
plt.title('Bar Plot')
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Data')
plt.show()