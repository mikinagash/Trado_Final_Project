import pytest
from Base.base import Base
from Pages.PStores import StoresPage
from Utils.utils import Utils
import pytest
from time import sleep



@pytest.mark.usefixtures('set_up')
class Test_Stores(Base):

#######ADD new store tests

#1
    def test_Add_store_correctly_when_insert_required_fields_only(self):
        driver=self.driver
        store= StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeName("shula")
        store.enter_storeCity("תל אביב")
        sleep(2)
        store.enter_storeStreet("השלום")
        sleep(2)
        store.enter_storeBuilding("12")
        store.click_addNewStore()

#2
    def test_Add_store_correctly_when_insert_all_fields(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_bnNumber()
        store.enter_storeName("h&m")
        store.enter_websiteUrl("www.h&m.com")
        store.enter_description("clothes store")
        store.enter_storePhone("0554536789")
        store.enter_storeEmail("hm@walla.com")
        store.enter_storeDepartment("shoes")
        store.enter_storeCity("ashdod")
        store.enter_storeStreet("hello")
        store.enter_storeBuilding("13")
        store.enter_storeApartment("167")
        store.click_addNewStore()

#3
    def test_Add_store_incorrectly_when_all_fieldsNull(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.click_addNewStore()

#4
    def test_Add_store_incorrectly_when_insert_only_optional_fields(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_bnNumber()
        store.enter_websiteUrl("www.h&m.com")
        store.enter_description("clothes store")
        store.enter_storePhone("0554536789")
        store.enter_storeEmail("hm@walla.com")
        store.enter_storeDepartment("shoes")
        store.enter_storeApartment("167")
        store.click_addNewStore()

#5
    def test_Add_store_incorrectly_when_insert_only_BnNumber(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_bnNumber()
        store.click_addNewStore()


#6
    def test_Add_store_incorrectly_when_insert_only_name(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeName("BBB")
        store.click_addNewStore()

#7
    def test_Add_store_incorrectly_when_insert_only_description(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_description("hey")
        store.click_addNewStore()

#8
    def test_Add_store_incorrectly_when_insert_only_telphone(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storePhone("0567345689")
        store.click_addNewStore()

#9
    def test_Add_store_incorrectly_when_insert_only_email(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeEmail("test1@gmail.com")
        store.click_addNewStore()

#10
    def test_Add_store_incorrectly_when_insert_only_department(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        sleep(3)
        store.enter_storeDepartment("שוקולדים")
        sleep(5)
        store.click_addNewStore()

#11
    def test_Add_store_incorrectly_when_insert_only_city(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeCity("ashkelon")
        store.click_addNewStore()

#12
    def test_Add_store_incorrectly_when_insert_only_street(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeStreet("מכבים 18")
        store.click_addNewStore()

#13
    def test_Add_store_incorrectly_when_insert_only_aprtment(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeApartment("145")
        store.click_addNewStore()

#14
    def test_Add_store_incorrectly_when_insert_only_buldingNum(self):
        driver = self.driver
        store = StoresPage(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.enter_storeBuilding("146")
        store.click_addNewStore()

###Search stores

#20
    def test_Display_store_details_correctly_when_searchBy_storeName(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("משה")

#21
    def test_Display_store_details_correctly_when_searchBy_storePhone(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("0547795920")

#22
    def test_Display_store_details_correctly_when_searchBy_storeEmail(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("dasda@jhj.com")

#23
    def test_Display_store_details_correctly_when_searchBy_partial_StoreName(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("sad")

#24
    def test_Display_store_details_correctly_when_searchBy_partial_storePhone(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("0455")

#25
    def test_Display_store_details_correctly_when_searchBy_partial_storeEmail(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("dasda")

#26
    def test_Display_store_details_incorrectly_when_searchBy_storeAddress(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("השלום")

#27
    def test_Display_store_details_incorrectly_when_searchBy_storeBnNumber(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("2214")

#28
    def test_Display_store_details_incorrectly_when_searchBy_createdDate(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("09/06/22")

#29
    def test_Display_store_details_incorrectly_when_searchBy_createdHour(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("11:18")

#30
    def test_Display_store_details_incorrectly_when_searchBy_department(self):
        driver = self.driver
        store = StoresPage(driver)
        store.search_store("שוקולדים")

#31








































