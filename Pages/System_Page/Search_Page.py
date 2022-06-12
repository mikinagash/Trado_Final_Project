# from Web.Locators.Home_Locators import HomeLocators
from selenium.webdriver.common.by import By

from Locators.System_Locators.LSystem_serch import SystemElement as EL
from time import sleep


class SystemPage:

    def __init__(self, driver):
        self.driver = driver
        self.phoneField = EL.phoneField
        self.phone = EL.phone
        self.clickSend = EL.clickSend
        self.passwordField = EL.passwordField
        self.password = EL.password
        self.clickLog = EL.clickLog
        self.btn_serch = EL.btn_serch
        self.serch_file = EL.search_field

    def entrance(self):
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
