# 核心执行器
# 1、获取数据
# 2、基于获取的数据，找到关键字，做对应的操作即可
from xToolkit import xfile
import pandas as pd
import pytest

# 所有的数据都取出来
# all_case = xfile.read(r"./resources/Test.xlsx").excel_to_dict(sheet_name='TestControl')
print("表格数据--标记")
# all_case = xfile.read(r".\resources\Test.xlsx").excel_to_dict(sheet_name=2)
all_case = pd.read_excel(r".\resources\Test.xlsx", sheet_name = 'TestControl')
print("表格数据：", all_case)


# 执行每一次，给到一行数据给case
@pytest.mark.parametrize('cases', all_case)
def test_excel(cases):
    print(cases)
