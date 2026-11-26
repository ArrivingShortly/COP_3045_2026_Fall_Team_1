### Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns


def operation(data, output_dir, histogram_data, histogram_title, histogram_xlabel, histogram_ylabel, plot_xlabel, plot_ylabel, plot_hue):
    """Generate the three automotive analysis visualizations."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Visualization 1: Selling price distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(
        data[histogram_data],
        kde=True,
        fill=True,
        color="teal",
    )
    plt.title(histogram_title)
    plt.xlabel(histogram_xlabel)
    plt.ylabel(histogram_ylabel)
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
        x=plot_xlabel,
        y=plot_ylabel,
        hue=plot_hue,
        data=data,
        alpha=0.6,
    )
    plt.title("Scatter Plot")
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)
    plt.tight_layout()
    plt.savefig(output_dir / "viz3_mileage_vs_price.png")
    plt.close()