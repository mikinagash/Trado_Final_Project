from Base.base import Base
from Pages.PReports import Report_Page
import pytest
from time import sleep
import requests
from Utils.Utils import Utils


@pytest.mark.usefixtures('set_up')
class Test_Reports(Base):

    # move between dates and verify the selected dates are displayed
    def test_something(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        reports.datesButton()
        # save dates in different lists
        value = reports.dates_static()
        # compare dates from diffrent lists
        assert value[0][0][:4] == "היום" \
               and value[0][1][:5] == "אתמול" \
               and value[0][2][-8:-3] == value[1][2][:5] or value[0][2][:-10] == value[2][2][:5] \
               and value[0][3][-8:-3] == value[1][3][:5] \
               and value[0][4][-8:-3] == value[1][4][:5] \
               and value[0][5][-8:-3] == value[1][5][:5]
        print(value)


    def test_sel_quick(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        reports.datesButton()
        reports.selectyear()
        sleep(2)
        reports.selectmonth(reports.leftscroldown,4)
        sleep(3)


    # verify logo img
    def test_ui_top_left_logo(self):
        driver = self.driver
        reports = Report_Page(driver)
        reports.open_reports_page()
        img = reports.trado_logo()
        assert img == reports.imglink


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

























####################################################################################
# ui sa ui  ui   ui   ui  ui


    # # verify logo img
    # def test_u1_pic(self):
    #     driver = self.driver
    #     reports = Report_Page(driver)
    #     reports.open_system_page()
    #     sleep(2)
    #     img = reports.trado_logo_1()
    #     assert img == "https://storage.cloud.google.com/trado_images/settings/value-2rnvbaw5joki7qm8ud?1607509995191"
    #
    # # verify  button text and size
    # def test_u2_logo(self):
    #     driver = self.driver
    #     reports = Report_Page(driver)
    #     reports.open_system_page()
    #     value = reports.reports_h4_logo_system()
    #     assert value[0] == "משתמשי מערכת" and value[1] == "26" and value[2] == "124"
    #
    # # #  verify button size
    # def test_u3_barsicon(self):
    #     driver = self.driver
    #     reports = Report_Page(driver)
    #     reports.open_system_page()
    #     value = reports.bars_icon_system()
    #     assert value[0] == "15" and value[1] == "15"
    #
    # def test_u3_serchfield_system(self):
    #     driver = self.driver
    #     reports = Report_Page(driver)
    #     reports.open_system_page()
    #     value = reports.serch_field()
    #     assert value[0] == "40" and value[1] == "188"
    #
    # def test_users_information_table(self):
    #     driver = self.driver
    #     reports = Report_Page(driver)
    #     reports.open_system_page()
    #     value = reports.information_table()
    #     print(len(value))
    #     print(type(value))
    #     print(value)


