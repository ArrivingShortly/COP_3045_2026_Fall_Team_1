### Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Visualization 1: Distribution of Car Prices
def create_histogram(column, dataset, name, xlab, ylab, export_file):
    if column:
        plt.figure(figsize=(8, 5))
        sns.histplot(dataset[column].dropna(), kde=True, fill=False, color='teal')
        plt.title(name)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.savefig(export_file)
        plt.close()
        print("Generated: " + export_file)


# Visualization 2: Correlation Heatmap
def create_correlation_heatmap(dataset, name, export_file):
    plt.figure(figsize=(8, 5))
    numeric_df = dataset.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        sns.heatmap(numeric_df.corr(), annot=True, cmap='viridis', fmt='.2f')
        plt.title(name)
        plt.savefig(export_file)
        plt.close()
        print("Generated: " + export_file)


# Visualization 3: Scatter Plot (Mileage vs Price)
def create_scatterplot(column1, column2, column3, dataset, name, xlab, ylab, export_file):
    if column1 and column2:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=column1, y=column2, data=dataset, alpha=0.6, hue=column3)
        plt.title(name)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.savefig(export_file)
        plt.close()
        print("Generated: viz3_mileage_vs_price.png")