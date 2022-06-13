from selenium.webdriver.common.by import By
from time import *


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


    # login to the site and open reports page
    def open_reports_page(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.enter_phone()
        reports.click_clickSend()
        sleep(0.5)
        reports.enter_passwordField()
        reports.click_clickSend()
        reports.enterReports()



    # enter a number into phone field
    def enter_phone(self):
        self.driver.find_element(By.XPATH,self.phoneField).send_keys(self.phone)


    # emter a number into a password field
    def enter_passwordField(self):
        self.driver.find_element(By.XPATH, self.passwordField).send_keys(self.password)


    # click send button
    def click_clickSend(self):
        self.driver.find_element(By.XPATH, self.clickSend).click()

    # click report page button
    def enterReports(self):
        self.driver.find_element(By.XPATH,self.reportsPageButton).click()


    # static ranges of calendar (incomplete)
    def staticRange(self):
        self.driver.find_element(By.XPATH,self.staticranges).click()


    # click dates button
    def datesButton(self):
        self.driver.find_element(By.XPATH,self.datesbutton).click()

    # click left button in the calendar
    def left_button_click(self):
        self.driver.find_element(By.XPATH,self.datesLeftButton).click()

    # click right button in the calendar
    def right_button_click(self):
        self.driver.find_element(By.XPATH,self.datesRightButton).click()

    # extract photo url from the logo
    def trado_logo(self):
        value = self.driver.find_element(By.XPATH,self.tradologo).get_attribute("src")
        return value

    # extract from logo name , size
    def reports_h4_logo(self):
        value = self.driver.find_element(By.XPATH,self.reportsh4logo).get_attribute("innerHTML")
        Height = self.driver.find_element(By.XPATH, self.reportsh4logo).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.reportsh4logo).get_attribute("clientWidth")
        return value ,Height ,Width

    # extract from bars icon size
    def bars_icon(self):
        Height = self.driver.find_element(By.XPATH, self.barsicon).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.barsicon).get_attribute("clientWidth")
        return Height , Width

    # extract from dates button size
    def date_display(self):
        Height = self.driver.find_element(By.XPATH, self.datesbutton).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.datesbutton).get_attribute("clientWidth")
        return Height , Width

    # extract from save button size , text
    def save_button(self):
        Height = self.driver.find_element(By.XPATH, self.saveButton).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.saveButton).get_attribute("clientWidth")
        vavlue = self.driver.find_element(By.XPATH, self.saveButton).get_attribute("innerHTML")
        return Height , Width ,vavlue
    # commit

    # unfinished
    # extract dates from the box

    # def dates_left_selected(self):
    #     v = self.driver.find_element(By.XPATH,self.datesLeftselected).get_attribute("innerHTML")
    #     return v
    #
    # def dates_left_selected(self):
    #     WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH,self.datesLeftselected))).get_attribute("innerHTML")
    #
    # def dates_right_selected(self):
    #     v = self.driver.find_element(By.XPATH,self.dates_right_selected()).get_attribute("innerHTML")
    #     return  v






