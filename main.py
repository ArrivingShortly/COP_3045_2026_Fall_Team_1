
"""Main entry point for the automotive data analysis application."""

from pathlib import Path
from data_configuration import DataConfiguration
from automotive_analysis.report import generate_report


def main():
    """Coordinate the complete automotive analysis workflow."""
    root = Path(__file__).resolve().parent
    output_dir = root / "output"
    process = DataConfiguration()

    try:
        print("--- 1. LOADING AND MERGING DATASETS ---")
        data = process.load_procedure()
        print(f"Combined records: {len(data):,}")

        print("\n--- 2. PREPARING DATA ---")
        data = process.clean_procedure()
        print(f"Cleaned records: {len(data):,}")

        print("\n--- 3. GENERATING VISUALIZATIONS ---")
        process.visualize_procedure()
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