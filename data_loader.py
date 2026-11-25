### Data loader
import pandas as pd


def operation(root, dataset1, dataset2):
    """Load and combine vehicle sales and specification datasets."""
    sales = pd.read_csv(root / dataset1)
    specs = pd.read_csv(root / dataset2)

    merged = sales.merge(
        specs,
        on=["Make", "Model", "Year"],
        how="inner",
        validate="many_to_one",
    )

    if merged.empty:
        raise ValueError("No matching vehicle records were found.")

    return merged