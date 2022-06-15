from selenium.webdriver.common.by import By
from time import *
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import Select





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
        self.driver.find_element(By.XPATH,self.lrdrStaticRange).click()


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


    # unfinished
    # random numbers from a to b
    # def rnd(self,a,b):
    #     n = randint(a,b)
    #     return n

    # click random element in objecet
    # def dates_static(self):
    #     s = self.driver.find_elements_by_xpath(self.staticranges)
    #     i = randint(0,len(s))
    #     return s[i].click() ,s[i].click(),s[i].click()
    # click on all fields


    # def dates_static(self):
    #     s = self.driver.find_elements_by_xpath(self.lrdrStaticRange)
    #     for i in range(len(s)):
    #         s[i].click()
    #         sleep(1)






    def dates_static(self):
        s = self.driver.find_elements_by_xpath(self.lrdrStaticRange)
        # b = self.driver.find_element(By.XPATH,self.datesbutton).get_attribute("innerHTML")
        for i in range(len(s)):
            s[i].click()
            a = self.driver.find_element(By.XPATH, self.datesbutton).get_attribute("innerText")
            b = self.driver.find_element(By.XPATH, self.datesLeftselected).get_attribute("value")
            c = self.driver.find_element(By.XPATH, self.dateRightselected).get_attribute("value")
            print(a)
    # 2 options, 0 = 2022 , 1 = 2021
    def selectyear(self):
        select = Select(self.driver.find_element_by_xpath(self.righhtscroldown))
        select.select_by_index(1)


    # 12 options,the current month is the limit for month selection
    # def selectmonth(self):
    #     select = Select(self.driver.find_element_by_xpath(self.leftscroldown))
    #     select.select_by_index(11)
    # same function
    # 12 options,the current month is the limit for month selection
    def selectmonth(self,element,index):
        select = Select(self.driver.find_element_by_xpath(element))
        select.select_by_index(index)














