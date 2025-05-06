# iris_analysis.py
# Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib
# Dataset: Iris dataset (loaded via sklearn.datasets)

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Set seaborn style for better visualization
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
print("=== Task 1: Load and Explore the Dataset ===")

# Load the Iris dataset
try:
    iris = load_iris()
    # Create a DataFrame from the dataset
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset (handle missing values, if any)
try:
    if df.isnull().sum().sum() > 0:
        print("\nFilling missing values with column means...")
        df.fillna(df.mean(numeric_only=True), inplace=True)
    else:
        print("\nNo missing values found.")
except Exception as e:
    print(f"Error handling missing values: {e}")

# Task 2: Basic Data Analysis
print("\n=== Task 2: Basic Data Analysis ===")

# Compute basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Perform grouping by species and compute the mean of numerical columns
print("\nMean of Numerical Columns by Species:")
group_means = df.groupby('species').mean()
print(group_means)

# Observations from analysis
print("\nObservations:")
print("- The dataset contains measurements of sepal and petal dimensions for three species of iris flowers.")
print("- From the group means, we observe that 'virginica' tends to have larger sepal and petal measurements compared to 'setosa' and 'versicolor'.")
print("- 'setosa' has the smallest petal length and width on average, which may help distinguish it from other species.")

# Task 3: Data Visualization
print("\n=== Task 3: Data Visualization ===")

# Create a figure with subplots
plt.figure(figsize=(15, 10))

# Visualization 1: Line chart (mean measurements per species)
plt.subplot(2, 2, 1)
group_means.plot(kind='line', marker='o')
plt.title('Mean Measurements per Species')
plt.xlabel('Species')
plt.ylabel('Measurement (cm)')
plt.legend(title='Features')
plt.xticks(ticks=range(len(group_means.index)), labels=group_means.index, rotation=45)

# Visualization 2: Bar chart (average petal length per species)
plt.subplot(2, 2, 2)
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.xticks(rotation=45)

# Visualization 3: Histogram (distribution of sepal length)
plt.subplot(2, 2, 3)
plt.hist(df['sepal length (cm)'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Sepal   # Save the figure
plt.savefig('outputs/iris_visualizations.png')
print("\nVisualizations saved as 'outputs/iris_visualizations.png'.")
