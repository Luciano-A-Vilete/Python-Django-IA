# test_app.py

def main():
    """
    Simple function to verify that the virtual environment is working and that dependencies are installed.
    """
    try:
        import numpy as np
        import pandas as pd
        print("Virtual environment is active and packages are installed correctly!")
        # Create a sample numpy array and dataframe
        arr = np.array([1, 2, 3, 4, 5])
        df = pd.DataFrame({'Numbers': arr})
        print("Sample DataFrame:")
        print(df)
    except ImportError as e:
        print("An import error occurred:", e)

if __name__ == "__main__":
    main()
