import pytest
import quantstats as qs
import pandas as pd
import numpy as np
import os
import tempfile


def test_html_report_no_mode_use_inf_as_null_error(sample_returns_series, sample_benchmark):
    """测试HTML报告生成不会抛出'mode.use_inf_as_null'错误"""
    # 创建临时文件以保存报告
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
        output_path = tmp.name
    
    try:
        # 尝试生成HTML报告
        html_content = qs.reports.html(
            sample_returns_series, 
            sample_benchmark, 
            benchmark_title='SPY', 
            output=output_path, 
            title='Test Report'
        )
        
        # 验证HTML内容被返回
        assert html_content is not None
        assert isinstance(html_content, str)
        assert len(html_content) > 0
        
        # 验证文件已创建并包含内容
        assert os.path.exists(output_path)
        assert os.path.getsize(output_path) > 0
        
    except Exception as e:
        # 如果发生错误，确保不是'mode.use_inf_as_null'错误
        error_msg = str(e)
        assert "mode.use_inf_as_null" not in error_msg, f"发生了'mode.use_inf_as_null'错误: {error_msg}"
        # 重新抛出其他错误
        raise
    finally:
        # 清理临时文件
        if os.path.exists(output_path):
            os.remove(output_path)