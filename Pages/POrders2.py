from selenium.webdriver.common.keys import Keys
import os.path
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LOrders2 import OrdersElement
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
        self.driver.find_element(By.XPATH, self.order_page_path).click()
        self.error_msg = OrdersElement.error_msg
        self.points_butten = OrdersElement.points_butten
        self.file_path = OrdersElement.file_path
        self.ready_path = OrdersElement.ready_path
        self.export = OrdersElement.export



    def enter_order(self, name):
        self.driver.find_element(By.XPATH, self.search).send_keys(name)



    def Error_msg(self):
        self.error = self.driver.find_element(By.XPATH, self.error_msg).get_attribute("innerText")
        return self.error




    def select_order(self):
        self.driver.find_element(By.XPATH, self.order).click()




    def export_files_received_order(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.export)))
        self.driver.find_element(By.XPATH, self.export).click()



    def export_files_Redy_order(self):
        self.driver.find_element(By.XPATH, self.ready_path).click()
        self.driver.find_element(By.XPATH, self.points_butten).click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH,self.export )))
        self.driver.find_element(By.XPATH, self.export).click()
        # while not os.path.exists(self.file_path):
        #     time.sleep(1)
        #
        # if os.path.isfile(self.file_path):
        #     print("file exesist")















