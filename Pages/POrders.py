import allure
import pytest
from selenium.webdriver.common.keys import Keys
from Locators.LOrders import OrdersElement
from selenium.webdriver.common.by import By
from time import sleep
from Locators.LOrders import OrdersElement



class OrdersPage(OrdersElement):

    def __init__(self,driver):
        self.driver = driver
        self.driver.find_element(By.XPATH, self.phoneField).send_keys("1950000000")
        sleep(3)
        self.driver.find_element(By.XPATH, self.clickSend).click()
        sleep(4)
        self.driver.find_element(By.XPATH, self.passwordField).send_keys("1234")
        sleep(4)
        self.driver.find_element(By.XPATH, self.clickLog).click()
        sleep(5)
        self.driver.get("https://qa-admin.trado.co.il/#/stores")
        self.search = OrdersElement.search
        self.order_page_path = OrdersPage.order_page_path




    def enter_order(self,name):
        self.driver.find_element(By.XPATH, self.order_page_path).click()
        self.driver.find_element(By.XPATH, self.search).send_keys(name)
        return self.driver.find_element(By.XPATH, self.table).get_attribute("innerText")








