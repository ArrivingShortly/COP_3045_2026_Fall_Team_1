### Data cleaner

def overall_operation(dataset):
    target_data = dataset.drop_duplicates()
    for col in target_data.select_dtypes(include=[np.number]).columns:
        target_data[col] = target_data[col].fillna(target_data[col].median())