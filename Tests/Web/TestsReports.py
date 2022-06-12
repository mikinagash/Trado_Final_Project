import Pages.pReports
from Base.base import Base
from Pages.pReports import Report_Page
import pytest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

staticranges = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"



@pytest.mark.usefixtures('set_up')
class Test_Reports(Base):


    def test_open(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.enter_phone()
        reports.click_clickSend()
        sleep(2)
        reports.enter_passwordField()
        reports.click_clickSend()
        reports.enterReports()

    def test_staticRanges(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.enter_phone()
        reports.click_clickSend()
        sleep(2)
        reports.enter_passwordField()
        reports.click_clickSend()
        reports.enterReports()
        sleep(2)
        reports.datesButton()
        sleep(3)
        value = driver.find_elements(By.XPATH,staticranges).get_attribute("innerText")
        print(len(value))
        print(value)
        print("asgdhfjfgjhgkhgkhlfhljhfljfhlf")











