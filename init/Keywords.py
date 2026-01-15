import time

# 封装我们web中常用的关键字内容
# 有多少个方法，就封装多少个
class Keywords:
    # 所有的操作均需要浏览器
    def __init__(self, driver):
        self.driver = driver    # 拿到浏览器

    # 浏览器去做具体的操作
    def open(self, **kwargs):
        self.driver.get(kwargs["数据内容"])

    def on_input(self, **kwargs):
        self.driver.find_element(kwargs["定位方式"], kwargs["目标对象"]).send_keys(kwargs["数据内容"])

    def on_click(self, **kwargs):
        self.driver.find_element(kwargs["定位方式"], kwargs["目标对象"]).click()

    @staticmethod
    def wait(**kwargs):
        time.sleep(kwargs["数据内容"])

    def on_getusername(self, **kwargs):
        actual_name = self.driver.find_element(kwargs["定位方式"], kwargs["目标对象"]).text
        print("获取到的页面用户名：", actual_name)
        expected_name = kwargs.get("数据内容")
        print("获取到的表格内容：", expected_name)
        assert actual_name == expected_name, f"文本不一致: 期望 {expected_name}, 实际 {actual_name}"
        return True, "文本一致"