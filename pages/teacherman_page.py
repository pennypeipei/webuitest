from common.base import Base
from common.config import host
from selenium import webdriver

login_url = host+"/xadmin/hello/teacherman/"

class TeachermanPage(Base):
    #左侧老师
    loc_1 = ("xpath",'//a[@href="/xadmin/hello/teacherman/"]')
    #新增老师
    loc_2 = ("xpath",'//a[@class="btn btn-primary"]')
    #输入新增老师信息
    loc_3_1 = ("id","id_teacher_name")
    loc_3_2 = ("id","id_tel")
    loc_3_3 = ("id","id_mail")
    loc_3_4 = ("xpath",'//div[contains(text(),"男")]')
    loc_3_5 = ("xpath",'//div[contains(text(),"女")]')
    #保存按钮
    loc_4 = ("xpath",'//button[@class="default btn btn-primary col-xs-10"]')
    js_1 = 'document.querySelector("#teacherman_form > div.form-actions.well.well-sm.clearfix > button > i").click();'
    css_1 = ("css selector","#teacherman_form > div.form-actions.well.well-sm.clearfix > button > i")
    #保存成功提示
    loc_5 = ("xpath",'//div[@class="alert alert-dismissable alert-success"]')

    def click_teacherman(self):
        '''点击左侧老师'''
        self.click(self.loc_1)

    def click_add_teacherman(self):
        '''点击新增老师'''
        self.click(self.loc_2)

    def inpt_teacherman(self):
        '''输入新增老师'''
        self.send(self.loc_3_1,"cccc")
        self.send(self.loc_3_2,"123456789")
        self.send(self.loc_3_3,"123@126.com")
        self.click(self.loc_3_4)
        self.click(self.loc_3_5)

    def save_teacherman(self):
        '''点击保存按钮'''
        self.click(self.css_1)

    def save_teacherman1(self):
        '''用JS点击'''
        self.driver.execute_script(self.js_1)

    def is_add_success(self,expect=''):
        '''判断是否添加成功，返回True/false'''
        get_result = self.get_text(self.loc_5)
        print("保存成功后页面信息为：%s"%get_result)
        return expect in get_result


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    #先登录
    from pages.login_page import LoginPage
    web = LoginPage(driver)
    web.login()

    teacher = TeachermanPage(driver)
    teacher.click_teacherman()
    teacher.click_add_teacherman()
    teacher.inpt_teacherman()
    teacher.save_teacherman1()
    res = teacher.is_add_success(expect="添加成功")
    print(res)
    driver.quit()
    assert res
    #driver.quit()
