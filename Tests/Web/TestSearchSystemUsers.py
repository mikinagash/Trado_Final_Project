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
        a = Utils(driver)
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.first_name_)
        name = driver.find_element(By.XPATH, EL.first_name_user).text
        a.validtion(name,EL.first_name_)
        # assert name == EL.first_name_

    def test_valid_serch_by_LastName(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.last_name_)
        name = driver.find_element(By.XPATH, EL.last_name_user).text
        assert name == EL.last_name_

    def test_valid_serch_by_email(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search("gg@hh.com")
        name = driver.find_element(By.XPATH, EL.email_user).text
        assert name == EL.email_

    def test_valid_serch_by_phone(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.phone_)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.phone_user).text
        assert name == EL.phone_

    def test_valid_serch_by_role(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.role_)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.role_user).text
        assert name == EL.role_

    def test_valid_serch_by_authorization(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.authorization_)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.authorization_user).text
        assert name == EL.authorization_2

    def test_invalid_serch_by_stores(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.stores_)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.stores_user).text
        assert name == EL.error_message

    def test_invalid_serch_by_last_seen(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.last_seen)
        sleep(1)
        name = driver.find_element(By.XPATH, EL.stores_user).text
        assert name == EL.error_message

    def test_invalid_serch_by_creation_date(self):
        driver = self.driver
        system = SystemPage(driver)
        system.Entrance()
        system.Btn_serch()
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
        system.Btn_serch()
        system.click_editing_system_user()
        system.editing_firstname()
        system.editing_lastname()
        system.editing_email()
        system.editing_phone()
        system.editing_role(3)
        # system.choose_role(2)
        sleep(6)