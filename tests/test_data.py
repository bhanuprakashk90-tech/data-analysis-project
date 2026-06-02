"""
Unit tests for data module
"""

import pytest
import pandas as pd
import numpy as np
from src.data import clean_data, handle_missing_values


class TestDataProcessing:
    """Test data processing functions"""
    
    @pytest.fixture
    def sample_df(self):
        """Create sample DataFrame for testing"""
        return pd.DataFrame({
            'A': [1, 2, np.nan, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 100, 300, 400, 500]
        })
    
    def test_handle_missing_values_mean(self, sample_df):
        """Test handling missing values with mean strategy"""
        result = handle_missing_values(sample_df, strategy='mean')
        assert result['A'].isnull().sum() == 0
        assert result['A'].iloc[2] == sample_df['A'].mean()
    
    def test_handle_missing_values_drop(self, sample_df):
        """Test handling missing values with drop strategy"""
        result = handle_missing_values(sample_df, strategy='drop')
        assert result.shape[0] == 4
        assert result.isnull().sum().sum() == 0
    
    def test_clean_data_removes_duplicates(self):
        """Test that clean_data removes duplicates"""
        df = pd.DataFrame({
            'A': [1, 2, 1],
            'B': [10, 20, 10]
        })
        result = clean_data(df, remove_duplicates=True, handle_missing=False)
        assert result.shape[0] == 2


if __name__ == '__main__':
    pytest.main([__file__])
