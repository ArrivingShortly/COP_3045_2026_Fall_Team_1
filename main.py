import os

import data_loader
import data_cleaner
import data_visualization



print("--- 1. LOADING REAL-WORLD CSV DATASETS ---")
# Verifies files and assigns datasets
df_specs = data_loader.initalize_data('vehicle_specs.csv')
df_sales = data_loader.initalize_data('car_sales.csv')

# Standardize column names if needed based on common Kaggle naming conventions
price_col = data_loader.find_col(df_sales, ['SellingPrice', 'Price', 'Selling_Price', 'MSRP'])
mileage_col = data_loader.find_col(df_sales, ['Mileage', 'Odometer', 'Kilometers', 'Miles'])
make_col = data_loader.find_col(df_sales, ['Make', 'Brand', 'Manufacturer'])
model_col = data_loader.find_col(df_sales, ['Model'])
year_col = data_loader.find_col(df_sales, ['Year', 'Model_Year'])

print(f"\nDetected columns -> Price: {price_col}, Mileage: {mileage_col}, Make: {make_col}, Model: {model_col}, Year: {year_col}")



print("\n--- 2. CLEANING & PREPARING DATA ---")
# Drop duplicates and fill missing numeric values
df_sales = data_cleaner.overall_operation(df_sales)



print("\n--- 3. GENERATING VISUALIZATIONS ---")
# Creates a histogram, correlation heatmap and scatterplot
data_visualization.create_histogram(price_col, df_sales, 'Distribution of Car Prices u', 'Price ($)', 'Count', 'viz1_selling_price.png')
data_visualization.create_correlation_heatmap(df_sales, 'Correlation Heatmap u', 'viz2_correlation.png')
data_visualization.create_scatterplot(mileage_col, price_col, year_col, df_sales, 'Mileage & Year vs. Price u', 'Mileage', 'Price ($)', 'viz3_mileage_vs_price.png')


print("\nSuccess! Data analysis and chart generation complete.")