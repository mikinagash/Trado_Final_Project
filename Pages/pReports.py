from selenium.webdriver.common.by import By

import Locators.LReports
from Locators.LReports import Reports
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Report_Page(Reports):

    def __init__(self,driver):
        self.driver = driver
        self.phoneField = Reports.phoneField
        self.passwordField = Reports.passwordField
        self.clickSend = Reports.clickSend

    # login
    def enter_phone(self):
        self.driver.find_element(By.XPATH,self.phoneField).send_keys(self.phone)


    def enter_passwordField(self):
        self.driver.find_element(By.XPATH, self.passwordField).send_keys(self.password)




    # login
    def click_clickSend(self):
        self.driver.find_element(By.XPATH, self.clickSend).click()


    # Reports page
    def enterReports(self):
        self.driver.find_element(By.XPATH,self.reportsPageButton).click()


    # static ranges
    def staticRange(self):
        self.driver.find_element(By.XPATH,self.staticranges).click()

    # static ranges
    def datesButton(self):
        self.driver.find_element(By.XPATH,self.datesbutton).click()











