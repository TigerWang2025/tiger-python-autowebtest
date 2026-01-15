from datetime import datetime

import pytest
import os
import subprocess
import sys


def generate_test_report():
    """生成HTML测试报告"""
    # 安装pytest-html插件
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest-html"])

    # 检查是否有 report 这个目录，如果没有此目录，先创建
    report_dir = "report"
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    # 运行测试并生成报告
    # report_path = "test_report.html"  # 直接生成名称为：test_report.html 的报告名
    # 运行测试并生成报告，报告名称带日期、带时间戳
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"test_report_{timestamp}.html"
    report_path = os.path.join(report_dir, report_filename)
    pytest.main(["-v", "--html=" + report_path, "--self-contained-html"])

    print(f"测试报告已生成: {report_path}")
    return report_path