# Clean and validate the combined automotive dataset before analysis.

import pandas as pd


def operation(data: pd.DataFrame) -> pd.DataFrame:
    """Clean duplicates, normalize text fields, and impute numeric missing values."""
    # Validate that input is a non-empty DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected 'data' to be a pandas DataFrame.")
    if data.empty:
        raise ValueError("Input DataFrame is empty; nothing to clean.")

    # Remove duplicate rows and work on an explicit copy
    cleaned = data.drop_duplicates().copy()

    # Strip leading/trailing whitespace from string/object columns
    for column in cleaned.select_dtypes(include=["object", "string"]).columns:
        cleaned[column] = cleaned[column].apply(
            lambda val: val.strip() if isinstance(val, str) else val
        )

    # Fill missing numeric values with each column's median
    for column in cleaned.select_dtypes(include="number").columns:
        if cleaned[column].isna().all():
            continue
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    # Confirm rows remain after cleaning
    if cleaned.empty:
        raise ValueError("Cleaned DataFrame has no rows remaining.")

    return cleaned