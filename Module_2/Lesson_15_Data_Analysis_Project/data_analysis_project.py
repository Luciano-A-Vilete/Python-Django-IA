"""
data_analysis_project.py

A practical data analysis project that demonstrates a full data workflow:
1. Generating a sample dataset,
2. Cleaning missing data,
3. Analyzing data by grouping,
4. Visualizing the results using a bar chart.

This project uses pandas, NumPy, matplotlib, and seaborn.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_sample_data(num_rows: int = 500) -> pd.DataFrame:
    """
    Generate a sample dataset with random data.

    Parameters:
        num_rows (int): Number of rows of data to generate.
    
    Returns:
        pd.DataFrame: A DataFrame containing sample data with columns 'Category', 'Value', and 'Date'.
    """
    np.random.seed(42)
    categories = ['A', 'B', 'C']
    data = {
        'Category': np.random.choice(categories, size=num_rows),
        'Value': np.random.randint(1, 100, size=num_rows),
        'Date': pd.date_range(start='2022-01-01', periods=num_rows, freq='D')
    }
    df = pd.DataFrame(data)
    
    # Introduce some missing values in 'Value'
    missing_indices = np.random.choice(df.index, size=5, replace=False)
    df.loc[missing_indices, 'Value'] = np.nan
    
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the provided DataFrame by handling missing values.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame with missing 'Value' filled with the column mean.
    """
    value_mean = df['Value'].mean()
    df['Value'].fillna(value_mean, inplace=True)
    return df

def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform descriptive analysis on the DataFrame by grouping data by 'Category'
    and calculating the count and average value.

    Parameters:
        df (pd.DataFrame): The cleaned DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame with average values per category.
    """
    summary = df.groupby('Category').agg(
        count=('Value', 'count'),
        average_value=('Value', 'mean')
    ).reset_index()
    return summary

def plot_data(summary: pd.DataFrame) -> None:
    """
    Plot the average values per category as a bar chart.

    Parameters:
        summary (pd.DataFrame): The summary DataFrame containing averages per category.
    
    Returns:
        None: Saves the plot as 'average_value_by_category.png' and displays it.
    """
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Category', y='average_value', data=summary, palette='viridis')
    plt.title('Average Value by Category')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.tight_layout()
    plt.savefig('average_value_by_category.png')
    plt.show()

def main() -> None:
    """
    Main function to run the data analysis project.

    Steps:
    1. Generate sample data.
    2. Clean the data.
    3. Analyze the data.
    4. Plot the results.
    """
    print("Generating sample data...")
    df = generate_sample_data(100)
    print("Sample data generated:")
    print(df.head())
    
    print("\nCleaning data...")
    df_clean = clean_data(df)
    print("Data after cleaning:")
    print(df_clean.head())
    
    print("\nAnalyzing data...")
    summary = analyze_data(df_clean)
    print("Analysis summary:")
    print(summary)
    
    print("\nPlotting data...")
    plot_data(summary)
    print("Plot saved as 'average_value_by_category.png'.")

if __name__ == "__main__":
    main()
