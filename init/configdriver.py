# configdriver.py 文件不能改动，它是pytest框架配置文件，是测试框架
# 提前安装 ： pip install pytest
# 提前安装 ： pip install selenium
from _pytest.fixtures import fixture


@pytest fixture(scope='session', autouse=True)
def driver():
    # 定义为全局变量
    global driver
    # 生成浏览器 -谷歌、火狐、IE、Edge、Safari
    driver = webdriver.Chrome()  #谷歌  --提前下载好驱动，可直接百度

    #基于浏览器去做一系列的动作，具体动作不定，包括：登录、注册、查询、查看小说、搜索...

    # 返回浏览器，让它去做测试用例中设置的具体内容
    yield driver
    # 关闭浏览器
    driver.quit()