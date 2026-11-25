### Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns


def operation(data, output_dir):
    """Generate the three automotive analysis visualizations."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Visualization 1: Selling price distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(
        data["SellingPrice"],
        kde=True,
        fill=True,
        color="teal",
    )
    plt.title("Distribution of Car Prices")
    plt.xlabel("Price ($)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_dir / "viz1_selling_price.png")
    plt.close()

    # Visualization 2: Correlation heatmap
    plt.figure(figsize=(8, 5))
    numeric_data = data.select_dtypes(include="number")
    sns.heatmap(
        numeric_data.corr(),
        annot=True,
        cmap="Blues",
        fmt=".2f",
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_dir / "viz2_correlation.png")
    plt.close()

    # Visualization 3: Mileage versus selling price
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        x="Mileage",
        y="SellingPrice",
        hue="Year",
        data=data,
        alpha=0.6,
    )
    plt.title("Mileage vs. Selling Price")
    plt.xlabel("Mileage")
    plt.ylabel("Price ($)")
    plt.tight_layout()
    plt.savefig(output_dir / "viz3_mileage_vs_price.png")
    plt.close()