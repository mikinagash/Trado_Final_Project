from time import sleep
from selenium.webdriver.common.by import By
from Pages.System_Page.Search_Page import SystemPage
from Base.base import Base
import pytest
from Locators.System_Locators.LSystem_serch import SystemElement as EL
import allure
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('set_up')
class Test_serch(Base):

    def test_valid_serch_by_FirstName(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.first_name_)
        name = driver.find_element(By.XPATH,EL.first_name_user).text
        assert name == EL.first_name_

    def test_valid_serch_by_LastName(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.last_name_)
        name = driver.find_element(By.XPATH,EL.last_name_user).text
        assert name == EL.last_name_

    def test_valid_serch_by_email(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search("gg@hh.com")
        name = driver.find_element(By.XPATH,EL.email_user).text
        assert name == EL.email_

    def test_valid_serch_by_phone(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.phone_)
        sleep(1)
        name = driver.find_element(By.XPATH,EL.phone_user).text
        assert name == EL.phone_

    def test_valid_serch_by_role(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.role_)
        sleep(1)
        name = driver.find_element(By.XPATH,EL.role_user).text
        assert name == EL.role_

    def test_valid_serch_by_authorization(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.authorization_)
        sleep(1)
        name = driver.find_element(By.XPATH,EL.authorization_user).text
        assert name == EL.authorization_2

    def test_invalid_serch_by_stores(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.stores_)
        sleep(1)
        name = driver.find_element(By.XPATH,EL.stores_user).text
        assert name == EL.error_message

    def test_invalid_serch_by_last_seen(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.last_seen)
        sleep(1)
        name = driver.find_element(By.XPATH,EL.stores_user).text
        assert name == EL.error_message

    def test_invalid_serch_by_creation_date(self):
        driver = self.driver
        system = SystemPage(driver)
        system.entrance()
        system.Btn_serch()
        system.click_serch_file()
        system.user_search(EL.creation_date)
        sleep(1)
        name = driver.find_element(By.XPATH,EL.stores_user).text
        assert name == EL.error_message


