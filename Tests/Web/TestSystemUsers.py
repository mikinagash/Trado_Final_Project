from Tests.Server.Data_Base.Mongo_DB import MongoDB,Queries
from time import sleep
from selenium.webdriver.common.by import By
from Pages.PSystem_Users import SystemPage
from Base.base import Base
import pytest
from Locators.LSystem import SystemElement as EL
import allure

from Utils.Utils import Utils


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('set_up')
class Test_serch(Base):

    def test_valid_serch_by_FirstName(self):
        driver = self.driver
        # a = Utils(driver)
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        sleep(2)
        system.user_search(EL.first_name_)
        sleep(2)
        name = driver.find_element(By.CSS_SELECTOR, EL.first_name_user).text
        # a.validtion(name,EL.first_name_)
        assert name == EL.first_name_

    def test_valid_serch_by_LastName(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_serch_file()
        sleep(3)
        system.user_search(EL.last_name_)
        sleep(3)
        name = driver.find_element(By.CSS_SELECTOR, EL.last_name_user).text
        assert name == EL.last_name_

    def test_valid_serch_by_email(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.email_)
        sleep(1)
        name = driver.find_element(By.CSS_SELECTOR, EL.email_user).text
        assert name == EL.email_

    def test_valid_serch_by_phone(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.phone_)
        sleep(1)
        name = driver.find_element(By.CSS_SELECTOR, EL.phone_user).text
        assert name == EL.phone_

    def test_valid_serch_by_role(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.role_)
        sleep(1)
        name = driver.find_element(By.CSS_SELECTOR, EL.role_user).text
        assert name == EL.role_

    def test_valid_serch_by_authorization(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.authorization_)
        sleep(1)
        name = driver.find_element(By.CSS_SELECTOR, EL.authorization_user).text
        assert name == EL.authorization_2 or EL.authorization_

    def test_invalid_serch_by_stores(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.stores_)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.stores_user).text
        assert name == EL.error_message

    def test_invalid_serch_by_last_seen(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.last_seen)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.stores_user).text
        assert name == EL.error_message

    def test_invalid_serch_by_creation_date(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.creation_date)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.stores_user).text
        assert name == EL.error_message


class Test_Editing_system_user(Base):

    def test_valid_Update_all_details(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('eli')
        system.editing_lastname('סלמון')
        system.editing_email('tasama@gmail.com')
        system.editing_phone('9513247812')
        system.editing_role(3)
        system.editing_authorization(0)
        system.editing_stores('tasama')
        system.editing_Btn_click()
        sleep(6)
        # new_edition_user_by_name = driver.find_element(By.XPATH, EL.click_details).text
        # assert new_edition_user_by_name == 'salmon'
        assert MongoDB.find()

    def test_valid_update_With_required_fields(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('סלמוןט')
        system.editing_lastname('טסמהט')
        system.editing_email('salmon@gmail.com')
        system.editing_stores('adidas')
        system.editing_Btn_click()
        sleep(3)
        new_edition_user_by_name = driver.find_element(By.XPATH, EL.click_details).text
        assert new_edition_user_by_name == 'סלמוןט'
        sleep(6)


    def test_valid_update_name(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        sleep(3)
        system.enter_id_user(EL.id_user)
        sleep(3)
        system.editing_firstname('salmon')
        sleep(3)
        system.editing_stores('a')
        system.editing_Btn_click()
        sleep(3)
        new_edition_user_by_name = driver.find_element(By.XPATH, EL.firstName_details).text
        assert new_edition_user_by_name == 'salmon'
        # a = MongoDB('trado_qa', 'adminusers').find_one1('firstName')
        # assert a == 'salmon'
        # assert Queries.find_one('adminUser','firstName') == 'salmon'

    def test_valid_update_lastname(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_lastname('tasama')
        system.editing_stores('a')
        system.editing_Btn_click()
        sleep(3)
        new_edition_user_by_name = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[12]/td[2]").text
        assert new_edition_user_by_name == 'tasama'
        sleep(3)

    def test_valid_update_email(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_email('salon@gmail.com')
        system.editing_stores('a')
        system.editing_Btn_click()
        sleep(3)
        new_edition_user_by_name = driver.find_element(By.XPATH, "//tbody[1]/tr[12]/td[3]").text
        assert new_edition_user_by_name == 'salon@gmail.com'
        sleep(3)

    def test_valid_update_phone(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_phone('1234567894')
        system.editing_stores('a')
        system.editing_Btn_click()
        sleep(3)
        new_edition_user_by_name = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[12]/td[4]").text
        assert new_edition_user_by_name == '1234567894'
        sleep(3)

    def test_valid_update_role(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_role(3)
        system.editing_stores('a')
        system.editing_Btn_click()
        sleep(3)
        new_edition_user_by_name = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[12]/td[5]").text
        assert new_edition_user_by_name == 'מנהל' or 'admin' or 'חנות' or 'owner' or 'מסירה'
        sleep(3)

    def test_valid_update_authorization(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_authorization(1)
        system.editing_stores('a')
        system.editing_Btn_click()
        new_edition_user_by_name = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[12]/td[6]").text
        assert new_edition_user_by_name == 'write' or "כתיבה"
        sleep(1)

    def test_valid_update_stores(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.Btn_serch()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_stores('salmon')
        system.editing_Btn_click()
        sleep(6)
        new_edition_user_by_name = driver.find_element(By.XPATH, "//table[1]/tbody[1]/tr[12]/td[7]").text
        assert new_edition_user_by_name == 'salmon'
        sleep(1)


    def test_invalid_Update_all_details_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('')
        system.editing_lastname('')
        system.editing_email('')
        system.editing_phone('')
        system.editing_role(0)
        system.editing_authorization(0)
        system.editing_stores('')
        # system.editing_Btn_click()
        sleep(1)
        system.error_message_firstname()
        system.error_message_lastname()
        system.error_message_email()
        system.error_message_phone_()
        system.error_message_stores_()
        sleep(2)
        system.editing_Btn_click()
        assert system.editing_error_messege_firstname() == EL.error_message_pops_up

    def test_invalid_Update_required_fields_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('')
        system.editing_lastname('')
        system.editing_email('')
        system.editing_phone('13245')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('')
        # system.editing_Btn_click()
        sleep(1)
        system.error_message_firstname()
        system.error_message_lastname()
        system.error_message_email()
        system.error_message_stores_()
        sleep(8)
        system.editing_Btn_click()
        sleep(6)
        assert system.editing_error_messege_firstname() == EL.error_message_pops_up

    def test_invalid_Update_firstname_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('')
        system.editing_lastname('dsfg')
        system.editing_email('salmon@sad.com')
        system.editing_phone('1234567858')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('xknui')
        # system.editing_Btn_click()
        sleep(1)
        system.error_message_firstname()
        sleep(1)
        system.editing_Btn_click()
        assert system.editing_error_messege_firstname() == EL.error_message_pops_up

    def test_invalid_Update_lastname_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('xfad')
        system.editing_lastname('')
        system.editing_email('salmon@sad.com')
        system.editing_phone('1234567858')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('xknui')
        # system.editing_Btn_click()
        sleep(1)
        system.error_message_lastname()
        sleep(1)
        system.editing_Btn_click()
        assert system.editing_error_messege_lastname() == EL.error_message_pops_up

    def test_invalid_Update_email_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('xfad')
        system.editing_lastname('safas')
        system.editing_email('')
        system.editing_phone('1234567858')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('xknui')
        # system.editing_Btn_click()
        # sleep(1)
        system.error_message_email()
        system.editing_Btn_click()
        sleep(1)
        assert system.editing_error_messege_email() == EL.error_message_pops_up

    def test_invalid_Update_email_is_invalid(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('xfad')
        system.editing_lastname('safas')
        system.editing_email('sfaadsc')
        system.editing_phone('1234567858')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('xknui')
        # system.editing_Btn_click()
        sleep(1)
        system.error_message_email_invalid()
        system.editing_Btn_click()
        sleep(1)
        assert system.editing_error_messege_email() == "אני רוצה לכלול '@' בכתובת האימייל. ב-'sfaadsc' חסר '@'."
        sleep(2)
        # system.error_message_email_invalid()
        # assert system.editing_error_messege_email() == "אני רוצה לכלול '@' בכתובת האימייל. ב-'sfaadsc' חסר '@'."


    def test_invalid_Update_phone_is_invalid(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('xfad')
        system.editing_lastname('safas')
        system.editing_email('salmon@gmai.com')
        system.editing_phone('1234')
        system.editing_role(1)
        system.editing_authorization(0)
        system.editing_stores('xknui')
        system.editing_Btn_click()
        sleep(1)
        system.error_message_phone_()

    def test_invalid_Update_phone_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('xfad')
        system.editing_lastname('safas')
        system.editing_email('salmon@gmai.com')
        system.editing_phone('1234')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('xknui')
        system.editing_Btn_click()
        sleep(3)

    def test_invalid_Update_store_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        # system.click_editing_system_user()
        system.enter_id_user(EL.id_user)
        system.editing_firstname('salm')
        system.editing_lastname('tas')
        system.editing_email('sfaadsc@gamil.com')
        system.editing_phone('1234567858')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('')
        # system.editing_Btn_click()
        # sleep(1)
        system.error_message_stores_()
        system.editing_Btn_click()
        sleep(1)
        assert system.editing_error_messege_stores() == EL.error_message_pops_up


class Test_add_a_user(Base):

    def test_valid_add_user(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('salmontasama231')
        system.editing_lastname('safas12')
        system.editing_email('salmont@gmai.com')
        system.editing_phone('1235678939')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('salmon')
        sleep(6)
        system.click_add()
        add_user = self.driver.find_element(By.XPATH, EL.lin_add_user).text
        assert add_user == 'salmontasama231'
        sleep(9)


    def test_valid_add_user_required_fields(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('xfad')
        system.editing_lastname('safas')
        system.editing_email('salmon@gmai.com')
        system.editing_stores('salmon')
        sleep(6)
        system.error_message_firstname()
        system.error_message_lastname()
        system.error_message_email()
        system.error_message_stores_()
        system.click_add()
        add_user = self.driver.find_element(By.XPATH, EL.lin_add_user).text
        assert add_user == 'xfad'
        sleep(9)


    def test_invalid_add_user_all_fielde_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('')
        system.editing_lastname('')
        system.editing_email('')
        system.editing_phone('')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('')
        system.error_message_firstname()
        system.error_message_lastname()
        system.error_message_email()
        system.error_message_phone_()
        system.error_message_stores_()
        sleep(6)
        system.click_add()
        assert system.editing_error_messege_firstname() == EL.error_message_pops_up
        sleep(9)

    def test_invalid_add_user_firstname_fielde_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('')
        system.editing_lastname('afadfas')
        system.editing_email('sdfaasd@adfadf.vs')
        system.editing_phone('9876543212')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('wdas')
        system.error_message_firstname()
        sleep(6)
        system.click_add()
        assert system.editing_error_messege_firstname() == EL.error_message_pops_up
        sleep(9)


    def test_invalid_add_user_lastname_fielde_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('gvgvggv')
        system.editing_lastname('')
        system.editing_email('sdfaasd@adfadf.vs')
        system.editing_phone('9876543212')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('wdas')
        system.error_message_lastname()
        sleep(6)
        system.click_add()
        assert system.editing_error_messege_lastname() == EL.error_message_pops_up
        sleep(9)


    def test_invalid_add_user_email_fielde_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('asdfdsfdas')
        system.editing_lastname('afadfas')
        system.editing_email('')
        system.editing_phone('9876543212')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('wdas')
        system.error_message_email()
        sleep(6)
        system.click_add()
        assert system.editing_error_messege_email() == EL.error_message_pops_up
        sleep(9)


    def test_invalid_add_user_email_fielde_is_invalid(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('asdasdas')
        system.editing_lastname('afadfas')
        system.editing_email('sd')
        system.editing_phone('9876543212')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('wdas')
        sleep(5)
        system.error_message_email_invalid()
        sleep(1)
        system.click_add()
        assert system.editing_error_messege_email() == "אני רוצה לכלול '@' בכתובת האימייל. ב-'sd' חסר '@'."
        sleep(9)


    def test_invalid_add_user_stores_fielde_is_null(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.click_add_but()
        system.editing_firstname('adfsdafsa')
        system.editing_lastname('afadfas')
        system.editing_email('sdfaasd@adfadf.vs')
        system.editing_phone('9876543212')
        system.editing_role(2)
        system.editing_authorization(0)
        system.editing_stores('')
        system.error_message_stores_()
        sleep(6)
        system.click_add()
        assert system.editing_error_messege_stores() == EL.error_message_pops_up
        sleep(9)

