"""
Data loading and processing module
"""

from .loader import load_data, load_csv, load_json
from .processor import clean_data, handle_missing_values

__all__ = ['load_data', 'load_csv', 'load_json', 'clean_data', 'handle_missing_values']
