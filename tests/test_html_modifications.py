import pytest
import quantstats as qs
import pandas as pd
import os
import tempfile


def test_html_report_output_none(short_sample_returns):
    """测试output=None时返回HTML内容"""
    # 调用reports.html，output=None
    html_content = qs.reports.html(short_sample_returns, output=None)
    
    # 验证HTML内容被返回
    assert html_content is not None
    assert isinstance(html_content, str)
    assert len(html_content) > 0
    assert '<html' in html_content.lower()

def test_html_report_output_file(short_sample_returns):
    """测试指定output文件路径时保存到文件并返回HTML内容"""
    # 创建临时文件以保存报告
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
        output_path = tmp.name
    
    try:
        # 调用reports.html，指定output文件路径
        html_content = qs.reports.html(short_sample_returns, output=output_path)
        
        # 验证HTML内容被返回
        assert html_content is not None
        assert isinstance(html_content, str)
        assert len(html_content) > 0
        
        # 验证文件已创建并包含内容
        assert os.path.exists(output_path)
        assert os.path.getsize(output_path) > 0
        
        # 验证文件内容与返回的内容是否一致
        with open(output_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        # 由于HTML内容可能包含时间戳等动态内容，我们只检查部分内容
        assert html_content[:100] == file_content[:100]
        
    finally:
        # 清理临时文件
        if os.path.exists(output_path):
            os.remove(output_path)