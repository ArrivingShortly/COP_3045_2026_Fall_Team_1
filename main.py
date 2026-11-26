
"""Main entry point for the automotive data analysis application."""

from pathlib import Path

import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

import data_loader
import data_cleaner
import data_visualization

from automotive_analysis.report import generate_report

#def load_data(root: Path, dataset1="car_sales.csv", dataset2="vehicle_specs.csv"):
#    """Load and combine vehicle sales and specification datasets."""
#    sales = pd.read_csv(root / dataset1)
#    specs = pd.read_csv(root / dataset2)
#
#    merged = sales.merge(
#        specs,
#        on=["Make", "Model", "Year"],
#        how="inner",
#        validate="many_to_one",
#    )
#
#    if merged.empty:
#        raise ValueError("No matching vehicle records were found.")
#
#    return merged

#def prepare_data(data: pd.DataFrame):
#    """Perform basic cleaning of the combined dataset."""
#    cleaned = data.drop_duplicates().copy()
#
#    for column in cleaned.select_dtypes(include="number").columns:
#        cleaned[column] = cleaned[column].fillna(
#            cleaned[column].median()
#        )
#
#    return cleaned

#def generate_visualizations(data: pd.DataFrame, output_dir: Path):
#    """Generate the three automotive analysis visualizations."""
#    output_dir.mkdir(parents=True, exist_ok=True)
#
    # Visualization 1: Selling price distribution
#    plt.figure(figsize=(8, 5))
#    sns.histplot(
#        data["SellingPrice"],
#        kde=True,
#        fill=True,
#        color="teal",
#    )
#    plt.title("Distribution of Car Prices")
#    plt.xlabel("Price ($)")
#    plt.ylabel("Count")
#    plt.tight_layout()
#    plt.savefig(output_dir / "viz1_selling_price.png")
#    plt.close()

    # Visualization 2: Correlation heatmap
#    plt.figure(figsize=(8, 5))
#    numeric_data = data.select_dtypes(include="number")
#    sns.heatmap(
#        numeric_data.corr(),
#        annot=True,
#        cmap="Blues",
#        fmt=".2f",
#    )
#    plt.title("Correlation Heatmap")
#    plt.tight_layout()
#    plt.savefig(output_dir / "viz2_correlation.png")
#    plt.close()

    # Visualization 3: Mileage versus selling price
#    plt.figure(figsize=(8, 5))
#    sns.scatterplot(
#        x="Mileage",
#        y="SellingPrice",
#        hue="Year",
#        data=data,
#        alpha=0.6,
#    )
#    plt.title("Mileage vs. Selling Price")
#    plt.xlabel("Mileage")
#    plt.ylabel("Price ($)")
#    plt.tight_layout()
#    plt.savefig(output_dir / "viz3_mileage_vs_price.png")
#    plt.close()


def main():
    """Coordinate the complete automotive analysis workflow."""
    root = Path(__file__).resolve().parent
    output_dir = root / "output"

    try:
        print("--- 1. LOADING AND MERGING DATASETS ---")
        data = data_loader.operation(root, "car_sales.csv", "vehicle_specs.csv")
        print(f"Combined records: {len(data):,}")

        print("\n--- 2. PREPARING DATA ---")
        data = data_cleaner.operation(data)
        print(f"Cleaned records: {len(data):,}")
        
        print("\n--- 3. GENERATING VISUALIZATIONS ---")
        data_visualization.operation(data, output_dir)
        print("All three visualizations generated.")

        print("\n--- 4. GENERATING PDF REPORT ---")
        report_path = generate_report(
            data=data,
            chart_dir=output_dir,
            output_path=(
                output_dir / "Automotive_Data_Analysis_Report.pdf"
            ),
        )

        print(f"\nReport generated: {report_path}")
        print("Application completed successfully!")

    except (OSError, ValueError, TypeError, KeyError) as error:
        raise SystemExit(f"Application error: {error}") from error


if __name__ == "__main__":
    main()