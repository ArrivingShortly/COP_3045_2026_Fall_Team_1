# COP3045 Automotive Data Analysis Project

## Project Overview

This project is an automated data analysis and reporting application built for the COP3045 course. It uses real-world datasets (`car_sales.csv` and `vehicle_specs.csv`) to examine vehicle specifications and sales records, generate visual charts, and produce a PDF report.

## Files Included

- `main.py`: Coordinates loading, cleaning, visualization, and PDF report generation.
- `data_loader.py`: Loads and merges the vehicle sales and specification datasets.
- `data_cleaner.py`: Cleans duplicates, normalizes text fields, and imputes missing numeric values.
- `data_visualization.py`: Generates charts from the cleaned dataset.
- `automotive_analysis/report.py`: Calculates statistics and builds the PDF report (`Automotive_Data_Analysis_Report.pdf`).
- `generate_report.py`: Standalone report generation entry point.
- `car_sales.csv`: Historical records of used car sales.
- `vehicle_specs.csv`: Vehicle specifications and features.
- `environment.yml`: Conda environment configuration and required dependencies.

## Environment Setup

1. Clone the repository:
   `git clone [https://github.com/ArrivingShortly/COP_3045_2026_Fall_Team_1.git](https://github.com/ArrivingShortly/COP_3045_2026_Fall_Team_1.git)`
   `cd COP_3045_2026_Fall_Team_1`
2. Create and activate the Conda environment:
   `conda env create -f environment.yml`
   `conda activate project-env`

## Running the Application

Run the full pipeline from the project root:

`python main.py`

This loads both CSV datasets, cleans the data, generates the visualizations (`viz1_selling_price.png`, `viz2_correlation.png`, and `viz3_mileage_vs_price.png`), and outputs `Automotive_Data_Analysis_Report.pdf` in the `output/` directory.

If you need to generate the report separately, run:

`python generate_report.py`

## Verification

Tested on Windows using Anaconda and Python 3.10.22:

- Conda environment created and activated successfully.
- Both CSV datasets loaded and merged without errors.
- Visualizations and PDF report generated successfully.

These checks confirm the pipeline runs in the configured environment and do not independently verify all analytical edge cases or dataset completeness.