from appium.webdriver import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Trado_Finel_Project.Locators.LOrders import OrdersElement
from Trado_Finel_Project.Base.base import Base
from Trado_Finel_Project.Pages.POrders import OrdersPage
from time import sleep
import pytest

@pytest.mark.usefixtures('set_up')
class Test_Orders(Base):

    def test_connect_to_site(self):
        driver = self.driver
        order = OrdersPage(driver)
        order.enter_phone_and_pass("1950000000","1234")
        sleep(2)

    def test_valid_search_pyment_type_b2b(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("b2b")

    def test_valid_search_pyment_type_bank_transfer(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("bankTransfer")

    def test_valid_search_pyment_type_e_trado(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("etrado")

    def test_valid_search_order_number(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("470")

    def test_invalid_search_order_number(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("3")

    def test_switch_page(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.move_to_page()

    def test_ready_order_page(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_the_ready_to_order_page()

    def test_delivery_order_page(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_delivery_order_page()

    def test_end_order_page(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_end_order()

    def test_order_details(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()

    def test_change_product_quantity(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.change_quantity()
        order.select()

    def test_change_pallets_quantity(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.change_pallets_quantity()
        order.choose_pallets_q()

    def test_update_weight(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()


    def test_chang_status_order_from_accepted_to_ready_to_delivery(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.change_quantity()
        order.select()
        order.change_pallets_quantity()
        order.choose_pallets_q()
        sleep(3)
        order.click_weight()
        order.up_weight()
        order.to_ready_to_delivery()

    def test_chang_status_order_from_ready_to_delivery_to_on_delivery(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_the_ready_to_order_page()
        order.Disply_details()
        order.on_delivery_button()

    def test_chang_status_order_from_on_delivery_to_delivery_to_Reached_destination(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_delivery_order_page()
        order.Disply_details()
        order.Reached_to_destination()


