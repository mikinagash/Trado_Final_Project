from Base.base import Base
from Utils.Utils import Utils
from time import sleep
from Pages.POrders import OrdersPage
import pytest
@pytest.mark.usefixtures('set_up')
class TestOrders(Base):


    @pytest.mark.regression
    def test_search_order_correct_by_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("עדי")
        # print(len(OrdersElement.table))
        # a.validtion( len(OrdersElement.table > 1),len(OrdersElement.table > 1))

    def test_search_order_correct_by_partly_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("עד")

    def test_search_order_incorrect_by_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גגג")
        a.validtion("גגג",OrdersPage.Error_msg,"pic")
        print(OrdersPage.Error_msg)


    def test_search_order_correct_by_last_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גרובר")
        sleep(3)




    def test_search_order_incorrect_by_last_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גגג")


    def test_verify_user_can_order_details(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        order.select_order()























