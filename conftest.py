from selenium import webdriver
import pytest
from pages.login_page import LoginPage
import os
import allure
import sys
from selenium.webdriver.chrome.options import Options

_driver = None
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    '''获取每个用例状态的钩子函数'''
    # 获取钩子方法的调用结果
    out = yield
    rep = out.get_result()
    # 仅获取用例call执行结果是失败的情况，不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failure",mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = "(%s)"%item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        with allure.step("添加失败截图..."):
            allure.attach(_driver.get_screenshot_as_png(),"失败截图",allure.attachment_type.PNG)


@pytest.fixture(scope="session")
def driver():
    global _driver
    chrome_options = Options()
    if _driver==None:
        if "win" in sys.platform:
            print("当前系统是windows")
            _driver = webdriver.Chrome()
            _driver.maximize_window()
        else:
            print("当前系统是linux")
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            _driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    yield _driver
    _driver.quit()

@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login()
    return driver