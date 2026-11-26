# Data configuration: sets the parameters for loading, cleaning, and visualizing the automotive datasets.
from pathlib import Path
import data_loader
import data_cleaner
import data_visualization

class DataConfiguration:
    def __init__(self):
        self.load = None
        self.clean = None

    @property
    def load_procedure(self):
        root = Path(__file__).resolve().parent
        self.load = data_loader.operation(Path(root), "car_sales.csv", "vehicle_specs.csv", "Make", "Model", "Year")

    @property
    def clean_procedure(self):
        self.clean = data_cleaner.operation(self.load)

    def visualize_procedure(self):
        root = Path(__file__).resolve().parent
        output_dir = root / "output"
        data_visualization.operation(self.clean, output_dir, "SellingPrice", "Distribution of Car Prices", "Price ($)", "Count", "Mileage", "SellingPrice", "Year")