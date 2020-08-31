from selenium import webdriver
from pages.teacherman_page import TeachermanPage
import allure

@allure.feature("添加老师")
class TestTeacherman():
    @allure.title("添加女老师")
    def test_add_teacherman(self,login):
        driver = login
        teacher = TeachermanPage(driver)
        with allure.step("点击左侧老师"):
            teacher.click_teacherman()
        with allure.step("点击添加老师"):
            teacher.click_add_teacherman()
        with allure.step("输入老师"):
            teacher.inpt_teacherman()
        with allure.step("点击保存"):
            teacher.save_teacherman()
        with allure.step("获取实际结果"):
            result = teacher.is_add_success(expect="xx")
        assert result

