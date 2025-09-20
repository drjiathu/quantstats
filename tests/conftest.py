import pytest
import pandas as pd
import numpy as np
import quantstats as qs
from datetime import datetime, timedelta

@pytest.fixture
def sample_returns_series():
    """返回一个示例收益序列"""
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
    returns = pd.Series(np.random.randn(len(dates)) * 0.01, index=dates)
    return returns

@pytest.fixture
def sample_returns_dataframe(sample_returns_series):
    """返回一个示例收益DataFrame"""
    return pd.DataFrame({'returns': sample_returns_series})

@pytest.fixture
def sample_benchmark():
    """返回一个示例基准收益序列"""
    np.random.seed(43)
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
    benchmark = pd.Series(np.random.randn(len(dates)) * 0.008, index=dates)
    return benchmark

@pytest.fixture
def short_sample_returns():
    """返回一个较短的示例收益序列"""
    dates = pd.date_range('2020-01-01', periods=10)
    returns = pd.Series(
        [0.01, -0.005, 0.02, 0.015, -0.01, 0.005, 0.01, -0.005, 0.02, 0.01],
        index=dates
    )
    return returns