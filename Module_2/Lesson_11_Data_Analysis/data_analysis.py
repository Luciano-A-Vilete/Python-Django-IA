import numpy as np
import pandas as pd

def analyze_array():
    """
    Create a NumPy array and compute its basic statistics.
    
    Returns:
        None
    """
    arr = np.array([10, 20, 30, 40, 50])
    mean_val = np.mean(arr)
    sum_val = np.sum(arr)
    std_val = np.std(arr)
    
    print("NumPy Array Analysis:")
    print("Array:", arr)
    print("Mean:", mean_val)
    print("Sum:", sum_val)
    print("Standard Deviation:", std_val)
    
def create_dataframe():
    """
    Create a pandas DataFrame using sample data and print its descriptive statistics.
    
    Returns:
        None
    """
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
        "Salary": [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)
    
    print("\nPandas DataFrame:")
    print(df)
    print("\nDataFrame Description:")
    print(df.describe())

if __name__ == "__main__":
    analyze_array()
    create_dataframe()