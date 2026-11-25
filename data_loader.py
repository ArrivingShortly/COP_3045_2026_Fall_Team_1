### ???
import pandas as pd

print("--- 1. LOADING REAL-WORLD CSV DATASETS ---")

def verify_files():
    try:
        # Load the CSV files you placed in the folder
        df_specs = pd.read_csv('vehicle_specs.csv')
        df_sales = pd.read_csv('car_sales.csv')
        print("Successfully loaded CSV files!")
    except Exception as e:
        print(f"Error loading files: {e}")
        exit()
    print(f"Vehicle Specs columns: {list(df_specs.columns)}")
    print(f"Car Sales columns: {list(df_sales.columns)}")
    return None

# Helper function to find a column name regardless of casing/naming variations
def find_col(df, options):
    for col in df.columns:
        if col.lower() in [opt.lower() for opt in options]:
            return col
    return None