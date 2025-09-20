import pytest
import quantstats as qs
import pandas as pd
import os
import tempfile


def test_download_filename_none(short_sample_returns):
    """测试download_filename=None时的行为"""
    # 调用reports.html，download_filename=None
    html_content = qs.reports.html(short_sample_returns, download_filename=None)
    
    # 验证HTML内容被返回
    assert html_content is not None
    assert isinstance(html_content, str)
    assert len(html_content) > 0
    assert '<html' in html_content.lower()

def test_download_filename_set(short_sample_returns):
    """测试download_filename设置时的行为"""
    # 调用reports.html，设置download_filename
    download_name = "test-download.html"
    html_content = qs.reports.html(short_sample_returns, download_filename=download_name)
    
    # 验证HTML内容被返回
    assert html_content is not None
    assert isinstance(html_content, str)
    assert len(html_content) > 0
    # 注意：在非交互式环境中，download_filename参数主要影响返回的内容
    # 实际的文件下载行为通常只在浏览器或Jupyter环境中发生