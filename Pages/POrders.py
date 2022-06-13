from selenium.webdriver.common.keys import Keys

from Locators.LOrders import OrdersElement
from selenium.webdriver.common.by import By
from time import sleep



class OrdersPage(OrdersElement):

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.XPATH, self.phoneField).send_keys("1950000000")
        sleep(1)
        self.driver.find_element(By.XPATH, self.clickSend).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.passwordField).send_keys("1234")
        sleep(1)
        self.driver.find_element(By.XPATH, self.clickLog).click()
        sleep(1)
        self.driver.get("https://qa-admin.trado.co.il/#/stores")
        self.search = OrdersElement.search
        self.order_page_path = OrdersElement.order_page_path
        self.error_msg = OrdersElement.error_msg


    def enter_order(self, name):
        self.driver.find_element(By.XPATH, self.order_page_path).click()
        self.driver.find_element(By.XPATH, self.search).send_keys(name)

    def Error_msg(self):
        return self.driver.find_element(By.XPATH, self.error_msg).get_attribute("innerText")



    def select_order(self):
        self.driver.find_element(By.XPATH, self.order_page_path).click()
        self.driver.find_element(By.XPATH, self.order).click()








