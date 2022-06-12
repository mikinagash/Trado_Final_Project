import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://qa-admin.trado.co.il/#/stores")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://qa-admin.trado.co.il/#/stores")

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()