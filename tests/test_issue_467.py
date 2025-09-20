import pytest
import quantstats as qs
import pandas as pd
import numpy as np


def test_cvar_consistency(sample_returns_series, sample_returns_dataframe):
    """测试Series和DataFrame的CVaR计算结果是否一致"""
    # 测试Series的CVaR计算
    var_series = qs.stats.var(sample_returns_series)
    cvar_series = qs.stats.cvar(sample_returns_series)
    
    # 测试DataFrame的CVaR计算
    var_df = qs.stats.var(sample_returns_dataframe)
    cvar_df = qs.stats.cvar(sample_returns_dataframe)
    
    # 检查值是否匹配
    assert abs(cvar_series - cvar_df) < 1e-10, f"CVaR计算结果不一致: Series={cvar_series:.4%}, DataFrame={cvar_df:.4%}"
    
    # 验证metrics报告中的结果
    metrics = qs.reports.metrics(sample_returns_series, mode='full', display=False)
    
    # 检查VaR和CVaR是否在metrics中正确计算
    assert 'Daily Value-at-Risk' in metrics.index
    assert 'Expected Shortfall (cVaR)' in metrics.index
    
    # 手动计算CVaR以验证
    var_threshold = qs.stats.value_at_risk(sample_returns_series, sigma=1, confidence=0.95)
    below_var_series = sample_returns_series[sample_returns_series < var_threshold]
    cvar_manual_series = below_var_series.mean()
    
    # 确保手动计算结果与库计算结果一致
    assert abs(cvar_series - cvar_manual_series) < 1e-10, f"手动计算的CVaR与库计算的不一致: 手动={cvar_manual_series:.4%}, 库={cvar_series:.4%}"