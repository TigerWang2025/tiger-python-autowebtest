# 核心执行器
# 1、获取数据
# 2、基于获取的数据，找到关键字，做对应的操作即可
import pytest
from xToolkit import xfile

# 所有的数据都取出来
# all_case = xfile.read(r"./resources/Test.xlsx").excel_to_dict(sheet_name='TestControl')
# ########xls格式的表格，以下可以逐行打印########
# all_case = ExcelReader(r".\resources\Test001.xls").excel_to_dict('TestControl')
all_case = xfile.read(r".\resources\Test.xls").excel_to_dict(sheet=0)
print("表格数据：", all_case)


@pytest.mark.parametrize('cases', all_case)
def test_excel(cases, keywords):
    print(cases)  # 拿到每一行数据
    keys = cases["关键字"]  # 比如关键字为open

    # 在我们的关键字文件[keywords]当中找到这个keys：open
    try:
        # 内置属性，可以在类当中找到对应的方法
        funname = keywords.__getattribute__(keys)  # 一个方法
    except Exception as e:
        print(e)
    # 调用方法，方法名（参数）
    funname(**cases)

# all_case = pd.read_excel(r".\resources\Test.xlsx", sheet_name = 'TestControl')
# 逐行打印数据
# for index, row in all_case.iterrows():
#     print(f"行 {index + 1}: {row}")

# 执行每一次，给到一行数据给case
# @pytest.mark.parametrize('cases', all_case.to_dict(orient='records'))
# def test_excel(cases, keywords):
#     print(cases)    # 拿到每一行数据
#     keys = cases["关键字"]    # 比如关键字为open
#
#     # 在我们的关键字文件[keywords]当中找到这个keys：open
#     try:
#         # 内置属性，可以在类当中找到对应的方法
#         funname = keywords.__getattribute__(keys) # 一个方法
#     except Exception as e:
#         print(e)
#     # 调用方法，方法名（参数）
#     funname(**cases)
