### Data loader
import pandas as pd

print("--- 1. LOADING REAL-WORLD CSV DATASETS ---")

def initalize_data(csv_file):
    try:
        # Load the CSV files you placed in the folder
        result = pd.read_csv(csv_file)
        print("Successfully loaded CSV file!")
    except Exception as e:
        print(f"Error loading files: {e}")
        exit()
    print(f"Columns: {list(result.columns)}")
    return result

# Helper function to find a column name regardless of casing/naming variations
def find_col(df, options):
    for col in df.columns:
        if col.lower() in [opt.lower() for opt in options]:
            return col
    return None