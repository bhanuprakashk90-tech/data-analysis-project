"""
Statistical analysis functions
"""

import pandas as pd
import numpy as np
from scipy import stats


def get_basic_stats(df):
    """
    Get basic statistical summary
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
        
    Returns:
    --------
    pd.DataFrame
        Statistical summary
    """
    return df.describe()


def get_correlation(df, method='pearson'):
    """
    Calculate correlation between columns
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    method : str, default='pearson'
        Correlation method: 'pearson', 'spearman', 'kendall'
        
    Returns:
    --------
    pd.DataFrame
        Correlation matrix
    """
    return df.corr(method=method, numeric_only=True)


def perform_anova(*groups):
    """
    Perform one-way ANOVA test
    
    Parameters:
    -----------
    *groups : array-like
        Groups to compare
        
    Returns:
    --------
    dict
        ANOVA results with F-statistic and p-value
    """
    f_stat, p_value = stats.f_oneway(*groups)
    return {
        'f_statistic': f_stat,
        'p_value': p_value,
        'significant': p_value < 0.05
    }
