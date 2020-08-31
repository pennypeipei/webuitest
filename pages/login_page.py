from common.base import Base
from common.config import host
import allure

login_url = host+"/xadmin/"

class LoginPage(Base):
    '''登录页面'''
    loc_1 = ("id","id_username")
    loc_2 = ("id","id_password")
    loc_3 = ("xpath","//button[text()='登录']")

    @allure.step("输入账号")
    def input_user(self,text=''):
        '''输入账号'''
        self.send(self.loc_1,text)

    @allure.step("输入密码")
    def input_psw(self,text=''):
        '''输入密码'''
        self.send(self.loc_2,text)
    @allure.step("点击登录按钮")
    def click_button(self):
        '''点击登录按钮'''
        self.click(self.loc_3)
    @allure.step("打开登录-输入账号，密码-点登陆")
    def login(self,user="admin",psw="yoyo123456"):
        '''登录'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        self.click_button()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()

    driver.quit()





