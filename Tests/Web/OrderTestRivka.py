from selenium.webdriver.common.by import By
from Trado_Finel_Project.Locators.LocatorsRivka import OrdersElement
from Trado_Finel_Project.Base.base import Base
from Trado_Finel_Project.Pages.PagesRivka import OrdersPage
from time import sleep
import allure
import pytest
from Trado_Finel_Project.Tests.Server.Data_Base.Mongo_DB import Mongodb
from Trado_Finel_Project.Utils.Utils import Utils
import pymongo


@pytest.mark.usefixtures('set_up')
class Test_Orders(Base):

    def test_connect_to_site(self):
        driver = self.driver
        order = OrdersPage(driver)
        order.enter_phone_and_pass("1950000000","1234")
        order.Enter_to_order_page()
        sleep(2)

    def test_valid_search_pyment_type_b2b(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("b2b")

        name = driver.find_element(By.XPATH,OrdersElement.pyType).text
        assert name == "b2b"
        a.validtion("b2b",OrdersElement.pyType,"1")

    def test_valid_search_pyment_type_bank_transfer(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("bankTransfer")

        name = driver.find_element(By.XPATH, OrdersElement.pyType).text
        assert name == "bankTransfer"
        a.validtion("bankTransfer", OrdersElement.pyType,"2")


    def test_valid_search_pyment_type_e_trado(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("etrado")

        name = driver.find_element(By.XPATH, OrdersElement.pyType).text
        assert name == "etrado"
        a.validtion("etrado", OrdersElement.pyType,"3")

    def test_valid_search_order_number(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("470")

        name = driver.find_element(By.XPATH, OrdersElement.order_num_search).text
        assert name == "470"
        a.validtion("470", OrdersElement.order_num_search,"4")

    def test_invalid_search_order_number(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.click()
        order.search_correct_pyment_type("88ע")

        name = driver.find_element(By.XPATH, OrdersElement.no_result).text
        assert name == "מציג\nלעמוד"
        a.validtion("מציג\nלעמוד", OrdersElement.no_result,"5")


    def test_switch_page(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.move_to_page()

        name = driver.find_element(By.XPATH, OrdersElement.switch).text
        assert name == "מציג 51-100 מתוך 273 שורות"
        a.validtion("מציג 51-100 מתוך 273 שורות", OrdersElement.switch,"6")

    def test_ready_order_page(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_the_ready_to_order_page()

        name = driver.find_element(By.XPATH, OrdersElement.order_ready).text
        assert name == "מוכנה"
        a.validtion("מוכנה", OrdersElement.order_ready,"7")

    def test_delivery_order_page(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_delivery_order_page()

        name = driver.find_element(By.XPATH, OrdersElement.order_ready).text
        assert name == "במשלוח"
        a.validtion("במשלוח", OrdersElement.order_ready,"8")

    def test_end_order_page(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_end_order()

        name = driver.find_element(By.XPATH, OrdersElement.order_ready).text
        assert name == "סיום"
        a.validtion("סיום", OrdersElement.order_ready,"9")

    def test_order_details(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.search_correct_pyment_type("1e1xpmlil4dzq0jn")
        order.Disply_details()

        name = driver.find_element(By.XPATH, OrdersElement.Dis_details).text
        assert name == " מספר הזמנה: 487"
        a.validtion(" מספר הזמנה: 487", OrdersElement.order_ready,"10")
        # #BUG

    def test_change_product_quantity(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.change_quantity()
        order.select()
        sleep(3)

    def test_change_pallets_quantity(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.change_pallets_quantity()
        order.choose_pallets_q()
        order.assert_change_pallets()

    def test_update_weight(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()

    # בלי אסרט

    def test_chang_status_order_from_accepted_to_ready_to_delivery(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.change_quantity()
        order.select()
        order.change_pallets_quantity()
        order.choose_pallets_q()
        order.assert_change_pallets()
        sleep(3)
        order.click_weight()
        order.up_weight()
        order.to_ready_to_delivery()
        order.assert_new_status()

        name = driver.find_element(By.XPATH, OrdersElement.ready_to_delivery).text
        assert name == "סמן הזמנה כמוכנה למשלוח"
        a.validtion("סמן הזמנה כמוכנה למשלוח", OrdersElement.order_ready,"11")
    # BUG

    def test_chang_status_order_from_ready_to_delivery_to_on_delivery(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_the_ready_to_order_page()
        order.Disply_details()
        order.on_delivery_button()
        order.assert_new_status()

    def test_chang_status_order_from_on_delivery_to_delivery_to_Reached_destination(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Move_to_delivery_order_page()
        order.Disply_details()
        order.Reached_to_destination()
        order.assert_new_status()

    def test_chang_to_missing_product(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.Disply_details()
        order.miss_p()

        name = driver.find_element(By.XPATH, OrdersElement.Missing_product).text
        assert name == "חסר"
        a.validtion("חסר", OrdersElement.order_ready,"12")
        #BUG

    def test_chang_product(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        self.test_connect_to_site()
        order.search_correct_pyment_type("1e1xpmlil4dzq0jn")
        order.Disply_details()
        order.chang_p()

        name = driver.find_element(By.XPATH, OrdersElement.change_product).text
        assert name == "החלף"
        a.validtion("החלף", OrdersElement.order_ready,"13")

        name = driver.find_element(By.XPATH, OrdersElement.change_product_windows).text
        assert name == "החלפת המוצר: שמן למון קוש"
        a.validtion("החלפת המוצר: שמן למון קוש", OrdersElement.change_product_,"13")
        # BUG

    def test_ui_trado_logo(self):
        driver = self.driver
        order = OrdersPage(driver)
        self.test_connect_to_site()
        img = order.trado_logo()
        assert img == "https://storage.cloud.google.com/trado_images/settings/value-2rnvbaw5joki7qm8ud?1607509995191"

    def test_ui_orders_up_page(self):
        driver = self.driver
        self.test_connect_to_site()
        name = driver.find_element(By.XPATH, OrdersElement.orders).text
        assert name == "הזמנות"
        print(name)