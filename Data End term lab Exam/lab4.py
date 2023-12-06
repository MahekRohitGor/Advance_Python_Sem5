import numpy as np
import pandas as pd 
import os
import matplotlib.pyplot as plt 

cwd = os.getcwd()
path = os.path.join(cwd, "Q4.csv")

# To check if Q4.csv is present
if os.path.exists(path):
    # 1. Display rows of dataset
    df = pd.read_csv("Q4.csv")
    print(df.iloc[2:6])

    # 2. check for missing values of age
    print(df.isnull().sum())

    # 2. replacing missing value of age with mean value
    age_mean = df['age'].mean()
    df['age'].fillna(age_mean, inplace=True)
    print(df.isnull().sum())

    # 3. Display the records of dataset having maximum and minimum age
    data = df['age'].to_numpy()
    data1 = np.sort(data)
    print("Minimum age: ", data1[0])
    print("Maximum age: ", data1[-1])

    # 4. For age > 50
    age50 = df[df['age'] > 50]
    print(age50)

    # 5. Plot pie chart
    df_survived = df[df['survived'] == 1]
    mfc = df_survived["sex"].value_counts()
    print(mfc)
    plt.figure(figsize=(8,8))
    plt.pie(mfc, labels=mfc.index ,colors=["red", "skyblue"])
    plt.title("Male vs Female Survived")
    plt.show()


else:
    print("File does not exist")