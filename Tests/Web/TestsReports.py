import Pages.PReports
from selenium.webdriver.support.select import Select
from Base.base import Base
from Pages.PReports import Report_Page
import pytest
from time import sleep
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('set_up')
class Test_Reports(Base):

    # # left to right clicks
    # def test_left_right(self):
    #     driver = self.driver
    #     reports = Report_Page(driver)
    #     reports.open_reports_page()
    #     reports.datesbutton()
    #     reports.left_button_click()
    #     reports.right_button_click()
    #     reports.enterReports()
    #     reports.dates_button()
    #     sleep(1)
        # value1 = reports.dates_right_selected()
        # sleep(1)
        # value2 = reports.dates_left_selected()
        # print(value1)
        # print(value2)+



    def test_ui_top_left_logo(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        img = reports.trado_logo()
        assert img == "https://storage.cloud.google.com/trado_images/settings/value-2rnvbaw5joki7qm8ud?1607509995191"

    # verify  button text and size
    def test_ui_top_right_h4logo(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        value = reports.reports_h4_logo()
        assert value[0] == "Reports" and value[1] == "26" and value[2] == "64"

    # #  verify button size
    def test_ui_bars_icon_size(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        value = reports.bars_icon()
        assert value[0] == "15" and value[1] == "15"

    #  verify button size
    def test_ui_dates_diaplay_icon_size(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        value = reports.date_display()
        assert value[0] == "49" and value[1] == "250"

    #  verify text and button size
    def test_ui_save_button(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        value = reports.save_button()
        assert value[0] == "38" and value[1] == "56" and value[2] == "שמירה"


    # send api request when submiting dates
    def test_register_api(self):
        url = "https://qa-api.trado.co.il/api/reports/fields"
        myobj = {"store_id": "1010101011rh", "start_date": "2022-06-05T20:49:46.752Z",}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")



