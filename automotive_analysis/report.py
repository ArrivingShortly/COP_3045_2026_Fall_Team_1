
"""Generate PDF reports from automotive analysis results."""

from pathlib import Path
from xml.sax.saxutils import escape

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak,
)


def validate_data(data: pd.DataFrame) -> None:
    """Validate the dataset required for PDF reporting."""
    required_columns = {
        "Make", "Model", "Year", "Mileage",
        "SellingPrice", "Condition", "BodyType", "EngineSize"
    }

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Report data must be a pandas DataFrame.")

    if data.empty:
        raise ValueError("Cannot generate a report from an empty dataset.")

    missing = required_columns - set(data.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(sorted(missing))}"
        )

    for column in ("SellingPrice", "Mileage"):
        if not pd.api.types.is_numeric_dtype(data[column]):
            raise ValueError(f"{column} must contain numeric values.")

        if data[column].isna().any():
            raise ValueError(f"{column} contains missing values.")


def calculate_statistics(data: pd.DataFrame) -> list[list[str]]:
    """Calculate descriptive statistics from the supplied dataset."""
    prices = data["SellingPrice"]
    mileage = data["Mileage"]

    return [
        ["Statistic", "Value"],
        ["Total vehicle records", f"{len(data):,}"],
        ["Unique manufacturers", str(data["Make"].nunique())],
        ["Average selling price", f"${prices.mean():,.2f}"],
        ["Median selling price", f"${prices.median():,.2f}"],
        ["Minimum selling price", f"${prices.min():,.2f}"],
        ["Maximum selling price", f"${prices.max():,.2f}"],
        ["Price standard deviation", f"${prices.std():,.2f}"],
        ["Average mileage", f"{mileage.mean():,.0f}"],
        ["Median mileage", f"{mileage.median():,.0f}"],
    ]


def create_comparison(
    data: pd.DataFrame, category: str
) -> list[list[str]]:
    """Summarize vehicle counts and prices by category."""
    summary = (
        data.groupby(category, dropna=False)["SellingPrice"]
        .agg(["count", "mean", "median"])
        .sort_values("mean", ascending=False)
    )

    rows = [
        [category, "Count", "Average Price", "Median Price"]
    ]

    for name, row in summary.iterrows():
        rows.append([
            str(name),
            f"{int(row['count']):,}",
            f"${row['mean']:,.2f}",
            f"${row['median']:,.2f}",
        ])

    return rows


def create_table(rows: list[list[str]]) -> Table:
    """Create a consistently formatted PDF table."""
    table = Table(rows, repeatRows=1, hAlign="LEFT")

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24476B")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.whitesmoke, colors.white]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
    ]))

    return table


def calculate_findings(data: pd.DataFrame) -> list[str]:
    """Generate findings supported by calculated analytical results."""
    prices = data["SellingPrice"]
    correlation = data["Mileage"].corr(prices)

    make_prices = data.groupby("Make")["SellingPrice"].mean()
    highest_make = make_prices.idxmax()

    findings = [
        f"The dataset contains {len(data):,} vehicle records "
        f"with an average selling price of ${prices.mean():,.2f}.",

        f"The median selling price is ${prices.median():,.2f}, "
        f"while recorded prices range from ${prices.min():,.2f} "
        f"to ${prices.max():,.2f}.",

        f"{highest_make} has the highest average selling price "
        f"in this dataset at ${make_prices.max():,.2f}.",
    ]

    if pd.notna(correlation):
        findings.append(
            f"The Pearson correlation between mileage and selling "
            f"price is {correlation:.3f}. This describes a linear "
            f"association and does not establish causation."
        )
    else:
        findings.append(
            "The mileage-price correlation could not be calculated "
            "because of insufficient variation in the data."
        )

    return findings


def generate_report(
    data: pd.DataFrame,
    chart_dir: Path,
    output_path: Path
) -> Path:
    """Generate a PDF containing statistics, comparisons, and charts.

    Args:
        data: Cleaned automotive dataset.
        chart_dir: Directory containing generated visualizations.
        output_path: Destination of the generated PDF.

    Returns:
        Path to the generated PDF report.

    Raises:
        ValueError: If the supplied dataset is invalid.
        FileNotFoundError: If a required visualization is missing.
        OSError: If the report cannot be written.
    """
    validate_data(data)

    chart_dir = Path(chart_dir)
    output_path = Path(output_path)

    charts = [
        (
            "viz1_selling_price.png",
            "Distribution of Car Prices",
            "Distribution of recorded vehicle selling prices."
        ),
        (
            "viz2_correlation.png",
            "Correlation Heatmap",
            "Linear correlations between numerical variables."
        ),
        (
            "viz3_mileage_vs_price.png",
            "Mileage vs. Selling Price",
            "Relationship between mileage and selling price."
        ),
    ]

    for filename, _, _ in charts:
        if not (chart_dir / filename).is_file():
            raise FileNotFoundError(
                f"Required visualization not found: {filename}"
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(
        "Automotive Data Analysis Report", styles["Title"]
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("1. Project Overview", styles["Heading1"]))
    story.append(Paragraph(
        "This report presents descriptive statistics, categorical "
        "comparisons, and visualizations of automotive data. "
        "Numerical findings are calculated automatically from "
        "the supplied dataset.",
        styles["BodyText"]
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "2. Descriptive Statistics", styles["Heading1"]
    ))
    story.append(create_table(calculate_statistics(data)))

    story.append(PageBreak())

    story.append(Paragraph(
        "3. Categorical Analysis", styles["Heading1"]
    ))

    for category in ("Make", "Condition", "BodyType"):
        story.append(Paragraph(
            f"Selling Price by {category}", styles["Heading2"]
        ))
        story.append(create_table(create_comparison(data, category)))
        story.append(Spacer(1, 16))

    story.append(PageBreak())

    story.append(Paragraph("4. Visualizations", styles["Heading1"]))

    for index, (filename, title, caption) in enumerate(charts):
        if index > 0:
            story.append(PageBreak())

        story.append(Paragraph(title, styles["Heading2"]))

        chart = Image(str(chart_dir / filename))
        chart._restrictSize(460, 340)

        story.append(chart)
        story.append(Spacer(1, 8))
        story.append(Paragraph(caption, styles["BodyText"]))

    story.append(PageBreak())

    story.append(Paragraph(
        "5. Analytical Findings", styles["Heading1"]
    ))

    for finding in calculate_findings(data):
        story.append(Paragraph(escape(finding), styles["BodyText"]))
        story.append(Spacer(1, 10))

    story.append(Paragraph("6. Limitations", styles["Heading1"]))
    story.append(Paragraph(
        "The results describe the supplied dataset and may not "
        "represent the entire automotive market. Correlations do "
        "not establish causation, and this application does not "
        "implement a vehicle price prediction model.",
        styles["BodyText"]
    ))

    try:
        document = SimpleDocTemplate(
            str(output_path),
            pagesize=letter,
            title="Automotive Data Analysis Report",
        )
        document.build(story)
    except OSError as error:
        raise OSError(
            f"Unable to write PDF report: {output_path}"
        ) from error

    return output_path
