### Data cleaner

def operation(data):
    """Perform basic cleaning of the combined dataset."""
    cleaned = data.drop_duplicates().copy()
    
    for column in cleaned.select_dtypes(include="number").columns:
        cleaned[column] = cleaned[column].fillna(
            cleaned[column].median()
        )
    
    return cleaned