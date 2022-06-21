from Base.base import Base
from Tests.Server.Data_Base.Mongo_DB import Mongodb
from Utils.Utils import Utils
from Pages.POrders2 import OrdersPage
import pytest
@pytest.mark.usefixtures('set_up')
class TestOrders(Base):


    @pytest.mark.regression
    def test_search_order_correct_by_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("עדי")
        a.validtion(Mongodb.search_query(self, 'firstName', "עדי"), "עדי", "pic")
        print(Mongodb.search_query(self, 'firstName', "עדי"))





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
        a.validtion(Mongodb.search_query(self,'lastName',"גרובר"),"גרובר","pic")
        print(Mongodb.search_query(self,'lastName',"גרובר"))


    def test_search_order_incorrect_by_last_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גגג")
        a.validtion(Mongodb.search_query(self,'lastName','גגג'),"גגג",'pic')
        print(Mongodb.search_query(self,'lastName','גגג'))



    def test_verify_user_can_order_details(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        order.select_order()























