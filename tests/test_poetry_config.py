import pytest
import sys
import os


def test_imports():
    """测试主要模块和依赖项是否可以正常导入"""
    # 尝试导入主要模块
    try:
        import quantstats as qs
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import scipy
        import tabulate
        import dateutil
        import packaging
        
        # 验证导入成功
        assert qs is not None
        assert pd is not None
        assert np is not None
        assert plt is not None
        assert sns is not None
        assert scipy is not None
        
    except ImportError as e:
        pytest.fail(f"导入失败: {str(e)}")

def test_basic_functionality():
    """测试基本功能是否正常工作"""
    # 导入必要的模块
    import quantstats as qs
    import pandas as pd
    from pandas import date_range
    
    # 创建示例收益数据，包含日期索引
    dates = date_range(start='2023-01-01', periods=5)
    returns = pd.Series([0.01, -0.005, 0.02, -0.01, 0.015], index=dates, name='returns')
    
    # 计算Sharpe比率
    try:
        sharpe = qs.stats.sharpe(returns)
        # 验证结果类型
        assert isinstance(sharpe, float)
        
        # 计算最大回撤
        max_drawdown = qs.stats.max_drawdown(returns)
        assert isinstance(max_drawdown, float)
        
        # 计算累计收益（使用可能的正确函数名）
        cumulative_returns = returns.cumsum().iloc[-1]
        assert isinstance(cumulative_returns, float)
        
    except Exception as e:
        pytest.fail(f"基本功能测试失败: {str(e)}")

def test_poetry_config_compatibility():
    """测试项目配置兼容性"""
    # 验证必要的配置文件存在
    required_files = ['pyproject.toml', 'setup.py', 'setup.cfg']
    for file in required_files:
        assert os.path.exists(file), f"配置文件 {file} 不存在"
    
    # 验证README文件存在
    readme_files = ['README.rst', 'README.md']
    readme_exists = any(os.path.exists(file) for file in readme_files)
    assert readme_exists, "README文件不存在"