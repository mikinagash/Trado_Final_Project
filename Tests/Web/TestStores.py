import pytest
from Base.base import Base
from Pages.PStores import StoresPage
from Utils.Utils import Utils
import pytest
from time import sleep



@pytest.mark.usefixtures('set_up')
class Test_Stores(Base):

#######ADD new store tests

#1
    def test_Add_store_correctly_when_insert_required_fields_only(self):
        driver=self.driver
        store= StoresPage(driver)
        results= Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        sleep(4)
        store.add_store_form_requiredFields("BbB","tel-aviv","hadar","12")
        store.click_addNewStore()
        results.validtion(store.assName,"BbB","Tests/Web/Reports/pic")



#2
    def test_Add_store_correctly_when_insert_all_fields(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("www.jjhjgg.com","hello","0554356542","tete@walla.com","shoes","89")
        store.add_store_form_requiredFields("shula", "telaviv", "hadorom", "12")
        store.click_addNewStore()

#3
    def test_Add_store_incorrectly_when_all_fieldsNull(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.click_addNewStore()

#4
    def test_Add_store_incorrectly_when_insert_only_optional_fields(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("www.jjhjgg.com", "hello", "0554356542", "tete@walla.com", "shoes", "89")
        store.click_addNewStore()

#5
    def test_Add_store_incorrectly_when_insert_only_BnNumber(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        sleep(3)
        store.add_store_form_optionalFields("","","","","","")
        store.click_addNewStore()


#6
    def test_Add_store_incorrectly_when_insert_only_name(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("bbb","","","")
        store.click_addNewStore()

#7
    def test_Add_store_incorrectly_when_insert_only_description(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("","my website","","","","")
        store.click_addNewStore()

#8
    def test_Add_store_incorrectly_when_insert_only_telphone(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("", "", "0567896574", "", "", "")
        store.click_addNewStore()

#9
    def test_Add_store_incorrectly_when_insert_only_email(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("", "", "", "yryr@walla.com", "", "")
        store.click_addNewStore()

#10
    def test_Add_store_incorrectly_when_insert_only_department(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("", "", "", "", "shoes", "")
        store.click_addNewStore()

#11
    def test_Add_store_incorrectly_when_insert_only_city(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("","ashdod","","")
        store.click_addNewStore()

#12
    def test_Add_store_incorrectly_when_insert_only_street(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("","","dor","")
        store.click_addNewStore()

#13
    def test_Add_store_incorrectly_when_insert_only_aprtment(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("","","","","","89")
        store.click_addNewStore()

#14
    def test_Add_store_incorrectly_when_insert_only_buldingNum(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("","","","678")
        store.click_addNewStore()

###update store details
#17

    def test_Update_store_correctly_when_update_optional_fields(self):
        driver= self.driver
        store= StoresPage(driver)
        results = Utils(driver)
        store.click_on_store_name()
        store.clear_optional_fields()
        store.add_store_form_optionalFields("www.h.com","hello","0654563423","gg@walla.com","שוקולדים","45")
        store.click_update()


#18
    def test_Update_store_details_incorrectly_when_delete_required_fields(self):
        driver= self.driver
        store= StoresPage(driver)
        results = Utils(driver)
        store.click_on_store_name()
        store.clear_required_fields()
        store.click_update()

#19
    def test_Update_store_details_correctly_when_update_required_fields(self):
        driver= self.driver
        store= StoresPage(driver)
        results=Utils(driver)
        store.click_on_store_name()
        store.clear_required_fields()
        store.add_store_form_requiredFields("tit","Jaffa","dolll","12")
        store.click_update()
        results.validtion(store.assName,"titi","pic")
        results.validtion(store.assAddress,"dolll 12, jaffa","pic")




###Search stores

#20
    def test_Display_store_details_correctly_when_searchBy_storeName(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("משה")

#21
    def test_Display_store_details_correctly_when_searchBy_storePhone(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("0547795920")

#22
    def test_Display_store_details_correctly_when_searchBy_storeEmail(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("dasda@jhj.com")

#23
    def test_Display_store_details_correctly_when_searchBy_partial_StoreName(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("sad")

#24
    def test_Display_store_details_correctly_when_searchBy_partial_storePhone(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("0455")

#25
    def test_Display_store_details_correctly_when_searchBy_partial_storeEmail(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("dasda")

#26
    def test_Display_store_details_incorrectly_when_searchBy_storeAddress(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("השלום")

#27
    def test_Display_store_details_incorrectly_when_searchBy_storeBnNumber(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("2214")

#28
    def test_Display_store_details_incorrectly_when_searchBy_createdDate(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("09/06/22")

#29
    def test_Display_store_details_incorrectly_when_searchBy_createdHour(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("11:18")

#30
    def test_Display_store_details_incorrectly_when_searchBy_department(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("shoes")














































