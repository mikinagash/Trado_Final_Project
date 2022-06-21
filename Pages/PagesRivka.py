from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from Trado_Finel_Project.Locators.LocatorsRivka import OrdersElement
from time import sleep
from selenium.webdriver.common.keys import Keys

class OrdersPage(OrdersElement):

    def __init__(self,driver):
        self.driver = driver
        self.phoneField = OrdersElement.phoneField
        self.passwordField = OrdersElement.passwordField
        self.clickSend = OrdersElement.clickSend
        self.search_txt_box = OrdersElement.search
        self.click_txt_box = OrdersElement.click_search
        self.move_page = OrdersElement.switch_page
        self.ready = OrdersElement.ready_order
        self.delivery = OrdersElement.delivery_order
        self.end = OrdersElement.end_page
        self.order_details = OrdersElement.clicking_on_a_column
        self.quantity_product = OrdersPage.quantity
        self.selectq = OrdersElement.select_quantity
        self.pallets_quantity = OrdersElement.pallets
        self.se_pallets = OrdersElement.select_pallets
        self.status_to_delivery = OrdersElement.ready_to_delivery
        self.update_weight = OrdersElement.weight
        self.change_to_on_delivery=OrdersElement.on_delivery
        self.reached = OrdersElement.Reached_destination
        self.order_page = OrdersElement.enter_to_order_page
        self.missing = OrdersElement.Missing_product

    def enter_phone_and_pass(self,phone,password):
        self.driver.find_element(By.XPATH, self.phoneField).send_keys(phone)
        self.driver.find_element(By.XPATH, self.clickSend).click()
        sleep(3)
        self.driver.find_element(By.XPATH, self.passwordField).send_keys(password)
        self.driver.find_element(By.XPATH, self.clickLog).click()

    def click(self):
        self.driver.find_element(By.XPATH,self.click_txt_box).click()
        sleep(2)

    def search_correct_pyment_type(self,pym):
        self.driver.find_element(By.XPATH,self.search_txt_box).send_keys(pym)
        sleep(5)

    def move_to_page(self):
        self.driver.find_element(By.XPATH,self.move_page).click()
        sleep(3)

    def Move_to_the_ready_to_order_page(self):
        self.driver.find_element(By.XPATH,self.ready).click()
        sleep(3)

    def Move_to_delivery_order_page(self):
        self.driver.find_element(By.XPATH,self.delivery).click()
        sleep(3)

    def Move_to_end_order(self):
        self.driver.find_element(By.XPATH,self.end).click()
        sleep(3)

    def Disply_details(self):
        self.driver.find_element(By.XPATH,self.order_details).click()
        sleep(3)

    def change_quantity(self):
        self.driver.find_element(By.XPATH,self.quantity_product).click()

    def select(self):
        self.driver.find_element(By.XPATH,self.selectq).click()
        sleep(2)

    def change_pallets_quantity(self):
        self.driver.find_element(By.XPATH,self.pallets_quantity).click()
        sleep(2)

    def choose_pallets_q(self):
        self.driver.find_element(By.XPATH,self.se_pallets).click()
        sleep(3)

    def to_ready_to_delivery(self):
        self.driver.find_element(By.XPATH,self.status_to_delivery).click()
        sleep(2)

    def click_weight(self):
        self.driver.find_element(By.XPATH, self.update_weight).click()

    def up_weight(self):
        self.driver.find_element(By.XPATH,self.update_weight).send_keys(OrdersElement.wgt)

    def on_delivery_button(self):
        self.driver.find_element(By.XPATH,self.change_to_on_delivery).click()
        sleep(3)

    def Reached_to_destination(self):
        self.driver.find_element(By.XPATH,self.Reached_destination).click()
        sleep(3)

    def Enter_to_order_page(self):
        self.driver.find_element(By.XPATH,self.order_page).click()

    def miss_p(self):
        self.driver.find_element(By.XPATH,self.missing).click()
        sleep(2)

    def chang_p(self):
        self.driver.find_element(By.XPATH,self.change_product).click()
        sleep(2)

    def trado_logo(self):
        value = self.driver.find_element(By.XPATH, self.logo).get_attribute("src")
        return value

    def assert_change_pallets(self):
        name = self.driver.find_element(By.XPATH, OrdersElement.pallets_status).text
        assert name == "סטטוס משטחים עודכן בהצלחה"

    def assert_new_status(self):
        name = self.driver.find_element(By.XPATH, OrdersElement.new_status).text
        assert name == "סטטוס הזמנה עודכן בהצלחה"