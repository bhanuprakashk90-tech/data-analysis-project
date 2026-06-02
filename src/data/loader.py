"""
Data loading utilities for various file formats
"""

import pandas as pd
import json
from pathlib import Path


def load_data(filepath, **kwargs):
    """
    Load data from various file formats
    
    Parameters:
    -----------
    filepath : str
        Path to the data file
    **kwargs : dict
        Additional arguments to pass to the loader function
        
    Returns:
    --------
    pd.DataFrame
        Loaded data as a pandas DataFrame
        
    Raises:
    -------
    ValueError
        If file format is not supported
    """
    filepath = Path(filepath)
    
    if filepath.suffix == '.csv':
        return load_csv(filepath, **kwargs)
    elif filepath.suffix == '.json':
        return load_json(filepath, **kwargs)
    elif filepath.suffix in ['.xlsx', '.xls']:
        return load_excel(filepath, **kwargs)
    else:
        raise ValueError(f"Unsupported file format: {filepath.suffix}")


def load_csv(filepath, **kwargs):
    """Load data from CSV file"""
    return pd.read_csv(filepath, **kwargs)


def load_json(filepath, **kwargs):
    """Load data from JSON file"""
    return pd.read_json(filepath, **kwargs)


def load_excel(filepath, **kwargs):
    """Load data from Excel file"""
    return pd.read_excel(filepath, **kwargs)
