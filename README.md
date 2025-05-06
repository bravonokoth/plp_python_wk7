# Plp_python_wk7

This repository contains the code and outputs for the Week 7 Python assignment focused on data analysis with Pandas and visualization with Matplotlib. The assignment uses the Iris dataset to perform data loading, exploration, analysis, and visualization.

## Project Structure
- `iris_analysis.py`: Python script that loads the Iris dataset, performs data analysis, and generates visualizations.
- `outputs/`: Directory containing the generated visualization (`iris_visualizations.png`).
- `README.md`: Project description and instructions.

## Requirements
To run the script, install the required Python libraries:

pip install pandas matplotlib seaborn scikit-learn
How to Run
Clone the repository:

git clone https://github.com/bravonokoth/plp_python_wk7.git
cd plp_python_wk7
Run the Python script:

python iris_analysis.py

The script will generate visualizations saved in the outputs/ directory.

## Outputs

iris_visualizations.png: Contains four plots:
Line chart of mean measurements per species.
Bar chart of average petal length by species.
Histogram of sepal length distribution.
Scatter plot of sepal length vs. petal length.

## Analysis Findings
'Virginica' has the largest measurements across all features.
'Setosa' has the smallest petal length and width.
Sepal length is approximately normally distributed.
There is a positive correlation between sepal length and petal length, with distinct clusters for each species.
