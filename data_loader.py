### Data loader
import pandas as pd

def operation(source, dataset1, dataset2, label1, label2, label3):
    """Load and combine vehicle sales and specification datasets."""
    base_path = source
    path1 = base_path / dataset1
    path2 = base_path / dataset2

    if not path1.exists():
        raise FileNotFoundError(f"Missing dataset file: {path1}")
    if not path2.exists():
        raise FileNotFoundError(f"Missing dataset file: {path2}")

    sales = pd.read_csv(path1)
    specs = pd.read_csv(path2)

    # Merge on shared vehicle keys and confirm non-empty output
    merged = sales.merge(
        specs,
        on=[label1, label2, label3],
        how="inner",
        validate="many_to_one",
    )

    if merged.empty:
        raise ValueError("No matching vehicle records were found after merge.")

    return merged