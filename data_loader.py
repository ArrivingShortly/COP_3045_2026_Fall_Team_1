from pathlib import Path
import pandas as pd


def operation(
    root: Path,
    dataset1: str = "car_sales.csv",
    dataset2: str = "vehicle_specs.csv",
) -> pd.DataFrame:
    # Verify input CSV files exist before reading
    base_path = Path(root)
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
        on=["Make", "Model", "Year"],
        how="inner",
        validate="many_to_one",
    )

    if merged.empty:
        raise ValueError("No matching vehicle records were found after merge.")

    return merged