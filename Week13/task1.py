import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("air_quality.csv")

# Remove any duplicate rows
df = df.drop_duplicates()

# Check for missing values
missing_values = df.isna().sum()
print(missing_values)

# Remove the categorical column from the dataset
df.drop(["City"], axis=1, inplace=True)

# Fill in any missing values with the median of the column
# for column in df.columns:
#     df[column] = df[column].fillna(df[column].median())

# Normalize the data
from scipy import stats
def normalize(data):
    return (data - data.min()) / (data.max() - data.min())

normalized_data = df.apply(normalize)

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(normalized_data, df["target"], test_size=0.25, random_state=42)

# Save the preprocessed data
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

# Create some visualizations of the preprocessed data
sns.distplot(X_train["air_quality"])
plt.title("Distribution of air quality in training set")
plt.show()

sns.heatmap(X_train.corr(), annot=True)
plt.title("Correlation matrix of training set")
plt.show()
