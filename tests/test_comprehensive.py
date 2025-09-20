import pytest
import quantstats as qs
import pandas as pd
import numpy as np
import os
import tempfile


def test_version_info():
    """测试版本信息获取"""
    # 验证版本字符串格式
    version = qs.__version__
    assert isinstance(version, str)
    # 简单验证版本格式 x.y.z
    parts = version.split('.')
    assert len(parts) >= 2
    for part in parts:
        # 允许版本中包含alpha/beta等后缀
        num_part = part.split('rc')[0].split('a')[0].split('b')[0]
        assert num_part.isdigit()

def test_basic_metrics_calculation(short_sample_returns):
    """测试基本指标计算功能"""
    # 测试Sharpe比率计算
    sharpe = qs.stats.sharpe(short_sample_returns)
    assert isinstance(sharpe, float)
    
    # 测试最大回撤计算
    max_drawdown = qs.stats.max_drawdown(short_sample_returns)
    assert isinstance(max_drawdown, float)
    assert max_drawdown <= 0  # 最大回撤应该是负数或零
    
    # 测试波动率计算
    volatility = qs.stats.volatility(short_sample_returns)
    assert isinstance(volatility, float)
    assert volatility >= 0  # 波动率应该是非负数

def test_comprehensive_functionality(sample_returns_series, sample_returns_dataframe, sample_benchmark):
    """测试综合功能，包括issue #467和#468的修复验证"""
    # 测试CVaR计算一致性 (issue #467)
    cvar_series = qs.stats.cvar(sample_returns_series)
    cvar_df = qs.stats.cvar(sample_returns_dataframe)
    assert abs(cvar_series - cvar_df) < 1e-10, f"CVaR计算结果不一致: Series={cvar_series:.4%}, DataFrame={cvar_df:.4%}"
    
    # 测试HTML报告生成 (issue #468)
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
        output_path = tmp.name
    
    try:
        html_content = qs.reports.html(
            sample_returns_series, 
            sample_benchmark, 
            benchmark_title='SPY', 
            output=output_path, 
            title='Test Report'
        )
        
        # 验证没有'mode.use_inf_as_null'错误
        # 验证HTML内容被正确生成
        assert html_content is not None
        assert len(html_content) > 0
        assert os.path.exists(output_path)
        
    except Exception as e:
        assert "mode.use_inf_as_null" not in str(e), f"发生了'mode.use_inf_as_null'错误: {str(e)}"
        raise
    finally:
        if os.path.exists(output_path):
            os.remove(output_path)