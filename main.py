data_loader.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import data_loader


print("--- 1. LOADING REAL-WORLD CSV DATASETS ---")
data_loader.verify_files()

df_specs = pd.read_csv('vehicle_specs.csv')
df_sales = pd.read_csv('car_sales.csv')

# Standardize column names if needed based on common Kaggle naming conventions
price_col = data_loader.find_col(df_sales, ['SellingPrice', 'Price', 'Selling_Price', 'MSRP'])
mileage_col = data_loader.find_col(df_sales, ['Mileage', 'Odometer', 'Kilometers', 'Miles'])
make_col = data_loader.find_col(df_sales, ['Make', 'Brand', 'Manufacturer'])
model_col = data_loader.find_col(df_sales, ['Model'])
year_col = data_loader.find_col(df_sales, ['Year', 'Model_Year'])

print(f"\nDetected columns -> Price: {price_col}, Mileage: {mileage_col}, Make: {make_col}, Model: {model_col}, Year: {year_col}")



print("\n--- 2. CLEANING & PREPARING DATA ---")
# Drop duplicates and fill missing numeric values
df_sales = df_sales.drop_duplicates()
for col in df_sales.select_dtypes(include=[np.number]).columns:
    df_sales[col] = df_sales[col].fillna(df_sales[col].median())

print("\n--- 3. GENERATING VISUALIZATIONS ---")

# Visualization 1: Distribution of Car Prices
if price_col:
    plt.figure(figsize=(8, 5))
    sns.histplot(df_sales[price_col].dropna(), kde=True, fill=False, color='teal')
    plt.title('Distribution of Car Prices')
    plt.xlabel('Price ($)')
    plt.ylabel('Count')
    plt.savefig('viz1_selling_price.png')
    plt.close()
    print("Generated: viz1_selling_price.png")

# Visualization 2: Correlation Heatmap
plt.figure(figsize=(8, 5))
numeric_df = df_sales.select_dtypes(include=[np.number])
if not numeric_df.empty:
    sns.heatmap(numeric_df.corr(), annot=True, cmap='viridis', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.savefig('viz2_correlation.png')
    plt.close()
    print("Generated: viz2_correlation.png")

# Visualization 3: Scatter Plot (Mileage vs Price)
if mileage_col and price_col:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=mileage_col, y=price_col, data=df_sales, alpha=0.6, hue=year_col)
    plt.title('Mileage & Price vs. Price')
    plt.xlabel('Mileage')
    plt.ylabel('Price ($)')
    plt.savefig('viz3_mileage_vs_price.png')
    plt.close()
    print("Generated: viz3_mileage_vs_price.png")

print("\nSuccess! Data analysis and chart generation complete.")