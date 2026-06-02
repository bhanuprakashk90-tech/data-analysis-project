"""
Data processing and cleaning utilities
"""

import pandas as pd
import numpy as np


def clean_data(df, remove_duplicates=True, handle_missing=True):
    """
    Clean dataset by removing duplicates and handling missing values
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    remove_duplicates : bool, default=True
        Whether to remove duplicate rows
    handle_missing : bool, default=True
        Whether to handle missing values
        
    Returns:
    --------
    pd.DataFrame
        Cleaned DataFrame
    """
    df = df.copy()
    
    if remove_duplicates:
        df = df.drop_duplicates()
    
    if handle_missing:
        df = handle_missing_values(df)
    
    return df


def handle_missing_values(df, strategy='mean'):
    """
    Handle missing values in the dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    strategy : str, default='mean'
        Strategy to handle missing values: 'mean', 'median', 'forward_fill', 'drop'
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with handled missing values
    """
    df = df.copy()
    
    if strategy == 'mean':
        df = df.fillna(df.mean(numeric_only=True))
    elif strategy == 'median':
        df = df.fillna(df.median(numeric_only=True))
    elif strategy == 'forward_fill':
        df = df.fillna(method='ffill')
    elif strategy == 'drop':
        df = df.dropna()
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
    
    return df


def get_data_summary(df):
    """
    Get summary statistics of the dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
        
    Returns:
    --------
    dict
        Summary statistics
    """
    return {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'duplicates': df.duplicated().sum(),
        'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # in MB
    }
