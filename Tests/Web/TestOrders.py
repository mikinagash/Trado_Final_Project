from Base.base import Base
from Utils.Utils import Utils
from Locators.LOrders import OrdersElement
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
        sleep(5)
        search.enter_order("עדי")
        sleep(6)
        # print(len(OrdersElement.table))
        # a.validtion( len(OrdersElement.table > 1),len(OrdersElement.table > 1))


    def test_search_order_incorrect_by_first_name(self):
        driver = self.driver
        search = OrdersPage(driver)
        sleep(5)
        search.enter_order("גגג")
        sleep(6)
        print(len(OrdersElement.table))



