"""
Plotting functions for data visualization
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_distribution(df, column, bins=30, figsize=(10, 6)):
    """
    Plot distribution of a single column
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    column : str
        Column name to plot
    bins : int, default=30
        Number of bins for histogram
    figsize : tuple, default=(10, 6)
        Figure size
    """
    plt.figure(figsize=figsize)
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df, figsize=(10, 8)):
    """
    Plot correlation matrix heatmap
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    figsize : tuple, default=(10, 8)
        Figure size
    """
    plt.figure(figsize=figsize)
    corr_matrix = df.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()


def plot_scatter(df, x, y, figsize=(10, 6), hue=None):
    """
    Plot scatter plot
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    x : str
        Column name for x-axis
    y : str
        Column name for y-axis
    figsize : tuple, default=(10, 6)
        Figure size
    hue : str, optional
        Column name for color coding
    """
    plt.figure(figsize=figsize)
    sns.scatterplot(data=df, x=x, y=y, hue=hue)
    plt.title(f'{y} vs {x}')
    plt.tight_layout()
    plt.show()


def plot_line_chart(df, x, y, figsize=(10, 6)):
    """
    Plot line chart
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    x : str
        Column name for x-axis
    y : str
        Column name for y-axis
    figsize : tuple, default=(10, 6)
        Figure size
    """
    plt.figure(figsize=figsize)
    plt.plot(df[x], df[y], marker='o')
    plt.title(f'{y} over {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
