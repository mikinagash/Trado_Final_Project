import pytest
from selenium.webdriver.common.by import By
from Base.base import Base
from Pages.PStores import StoresPage
from Utils.Utils import Utils
import pytest
from time import sleep



@pytest.mark.usefixtures('set_up')
class Test_Stores(Base):

#######ADD new store tests


    # def test_upload(self):
    #     driver=self.driver
    #     store= StoresPage(driver)
    #     results= Utils(driver)
    #     store.click_add_buttonn()
    #     store.click_adding()
    #     store.upload_img()

#1
    def test_Add_store_correctly_when_insert_required_fields_only(self):
        driver=self.driver
        store= StoresPage(driver)
        results= Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("BB5","tel-aviv","hadar","12")
        store.click_addNewStore()
        asrt = store.verify_By_text(store.assName)
        # asrt=self.driver.find_element(By.XPATH,store.assName).text
        results.validtion(asrt,"BB5","8")


#2
    def test_Add_store_correctly_when_insert_all_fields(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("www.jjhjgg.com","hello","0554356542","tete@walla.com","shoes","89")
        store.add_store_form_requiredFields("shula", "telaviv", "hadorom", "12")
        results.validtion(store.assName,"shula","pic")
        store.click_addNewStore()
        asrt = store.verify_By_text(store.assName)
        results.validtion(asrt, "shula", "8")

#3
    def test_Add_store_incorrectly_when_all_fieldsNull(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה","pic")

#4
    def test_Add_store_incorrectly_when_insert_only_optional_fields(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("tredo", "hello", "0554356542", "tete@walla.com", "shoes", "89")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "pic")

#5
    def test_Add_store_incorrectly_when_insert_only_BnNumber(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("","","","","","")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "12")


#6
    def test_Add_store_incorrectly_when_insert_only_name(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("burgers","","","")
        store.click_addNewStore()
        asrt=store.verify_by_innerText(store.assErrorCity)
        results.validtion(asrt, "נא למלא שדה זה", "6")

#7
    def test_Add_store_incorrectly_when_insert_only_description(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("","my website","","","","")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "7")


#8
    def test_Add_store_incorrectly_when_insert_only_telphone(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("", "", "0567896574", "", "", "")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "8")



#9
    def test_Add_store_incorrectly_when_insert_only_email(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("", "", "", "yryr@walla.com", "", "")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "9")

#10
    def test_Add_store_incorrectly_when_insert_only_department(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("", "", "", "", "shoes", "")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "10")

#11
    def test_Add_store_incorrectly_when_insert_only_city(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("","ashdod","","")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "11")

#12
    def test_Add_store_incorrectly_when_insert_only_street(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("","","dor","")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "12")

#13
    def test_Add_store_incorrectly_when_insert_only_aprtment(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_optionalFields("","","","","","89")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "13")

#14
    def test_Add_store_incorrectly_when_insert_only_buldingNum(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.click_add_buttonn()
        store.click_adding()
        store.add_store_form_requiredFields("","","","678")
        store.click_addNewStore()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt, "נא למלא שדה זה", "14")




###update store details
#17

    def test_Update_store_correctly_when_update_optional_fields(self):
        driver= self.driver
        store= StoresPage(driver)
        results = Utils(driver)
        store.click_on_store_name()
        store.clear_optional_fields()
        store.add_store_form_optionalFields("web","hello","0654563423","netz@walla.com","שוקולדים","45")
        store.click_update()
        sleep(2)
        asrt = store.verify_By_text(store.assPhone)
        asrt1 = store.verify_By_text(store.assEmail)
        results.validtion(asrt,"0654563423","17")
        sleep(2)
        results.validtion(asrt1, "netz@walla.com", "117")


#18
    def test_Update_store_details_incorrectly_when_delete_required_fields(self):
        driver= self.driver
        store= StoresPage(driver)
        results = Utils(driver)
        store.click_on_store_name()
        store.clear_required_fields()
        store.click_update()
        asrt = store.verify_by_innerText(store.assError)
        results.validtion(asrt,"נא למלא שדה זה" ,"pic")

#19
    def test_Update_store_details_correctly_when_update_required_fields(self):
        driver= self.driver
        store= StoresPage(driver)
        results=Utils(driver)
        store.click_on_store_name()
        store.clear_required_fields()
        store.add_store_form_requiredFields("tomi","Jaffa","dor","13")
        store.click_update()
        asrt= store.verify_By_text(store.assName)
        sleep(2)
        results.validtion(asrt,"tomi","pic1")

###Search stores

#20
    def test_Display_store_details_correctly_when_searchBy_storeName(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("משה")
        sleep(2)
        asrt = store.verify_By_text(store.assName)
        # asrtName=self.driver.find_element(By.XPATH,"//td[contains(text(),'משה')]").text
        sleep(2)
        results.validtion(asrt,"משה","23")



#21
    def test_Display_store_details_correctly_when_searchBy_storePhone(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("0547795920")
        sleep(2)
        asrt = store.verify_By_text(store.assPhone)
        sleep(2)
        results.validtion(asrt,"0547795920","21")

#22
    def test_Display_store_details_correctly_when_searchBy_storeEmail(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("netz@")
        sleep(2)
        asrt = store.verify_By_text(store.assEmail)
        sleep(2)
        results.validtion(asrt, "netz@walla.com", "22")


#23
    def test_Display_store_details_correctly_when_searchBy_partial_StoreName(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("sad")
        sleep(2)
        asrt = store.verify_By_text(store.assName)
        sleep(2)
        # asrtName = self.driver.find_element(By.XPATH, "//td[contains(text(),'sadasds')]").text
        results.validtion(asrt, "sadasds", "23")


#24
    def test_Display_store_details_correctly_when_searchBy_partial_storePhone(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("05477")
        sleep(2)
        asrt = store.verify_By_text(store.assPhone)
        sleep(2)
        results.validtion(asrt, "0547795920", "24")

#25
    def test_Display_store_details_correctly_when_searchBy_partial_storeEmail(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("netz@")
        sleep(2)
        asrt = store.verify_By_text(store.assEmail)
        sleep(2)
        results.validtion(asrt, "netz@walla.com", "25")

#26
    def test_Display_store_details_incorrectly_when_searchBy_storeAddress(self):
        driver = self.driver
        store = StoresPage(driver)
        results = Utils(driver)
        store.search_store("השלום")
        asrtNoResults = self.driver.find_element(By.XPATH,"paging_paging").get_attribute("innerText")
        results.validtion(asrtNoResults,'מציג\nלעמוד\nאין תוצאות\nסה״כ: 0 שורות',"29")



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
        store.search_store("שוקולדים")














































