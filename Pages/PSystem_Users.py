# from Web.Locators.Home_Locators import HomeLocators
from selenium.webdriver.common.by import By

from Locators.LSystem import SystemElement as EL
from time import sleep
import select
from selenium.webdriver.support.ui import Select



class SystemPage:

    def __init__(self, driver):
        self.driver = driver
        self.phoneField = EL.phoneField
        self.phone = EL.phone
        self.clickSend = EL.clickSend
        self.passwordField = EL.passwordField
        self.password = EL.password
        self.clickLog = EL.clickLog
        self.btn_serch = EL.btn_system_users
        self.serch_file = EL.search_field
        self.clickDetails = EL.click_details
        self.firstname_user_editing = EL.editing_firstname_user
        self.lastname_user_editing = EL.editing_lastname_user
        self.email_user_editing = EL.editing_email_user
        self.phone_user_editing = EL.editing_phone_user
        self.role_user_editing = EL.editing_role_user
        # self.role_user_editing = EL.ad







    def Entrance(self):
        self.driver.find_element(By.XPATH, self.phoneField).send_keys(EL.phone)
        self.driver.find_element(By.XPATH, self.clickSend).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.passwordField).send_keys(EL.password)
        self.driver.find_element(By.XPATH, self.clickLog).click()

    def Btn_serch(self):
        self.driver.find_element(By.XPATH, self.btn_serch).click()


    def click_serch_file(self):
        self.driver.find_element(By.XPATH, self.serch_file).click()

    def user_search(self, details):
        self.driver.find_element(By.XPATH, self.serch_file).send_keys(details)


    # editing system user
    # def clear_file(self,file):
    #     self.driver.find_element(By.XPATH, file).clear()



    def click_editing_system_user(self):
        self.driver.find_element(By.XPATH, self.clickDetails).click()

    def editing_firstname(self):
        self.driver.find_element(By.XPATH, self.firstname_user_editing).click()
        self.driver.find_element(By.XPATH, self.firstname_user_editing).clear()
        # self.clear_file("firstname_user_editing")
        self.driver.find_element(By.XPATH, self.firstname_user_editing).send_keys(EL.new_firstname)

    def editing_lastname(self):
        self.driver.find_element(By.XPATH, self.lastname_user_editing).click()
        self.driver.find_element(By.XPATH, self.lastname_user_editing).clear()
        self.driver.find_element(By.XPATH, self.lastname_user_editing).send_keys(EL.new_lastname)

    def editing_email(self):
        self.driver.find_element(By.XPATH, self.email_user_editing).click()
        self.driver.find_element(By.XPATH, self.email_user_editing).clear()
        self.driver.find_element(By.XPATH, self.email_user_editing).send_keys(EL.new_email)

    def editing_phone(self):
        self.driver.find_element(By.XPATH, self.phone_user_editing).click()
        self.driver.find_element(By.XPATH, self.phone_user_editing).clear()
        self.driver.find_element(By.XPATH, self.phone_user_editing).send_keys(EL.new_phone)

    def editing_role(self,num):
        self.driver.find_element(By.XPATH, self.role_user_editing).click()
        roles = self.driver.find_elements(By.XPATH, EL.index_roles)
        roles[num].click()

    def editing_authorization(self,num):
        self.driver.find_element(By.XPATH, self.editing_authorization()).click()
        roles = self.driver.find_elements(By.XPATH, EL.index_authorization)
        roles[num].click()


    # def choose_role(self, num):
    #     roles = self.driver.find_elements(By.XPATH, EL.roles)
    #     roles[num].click()






