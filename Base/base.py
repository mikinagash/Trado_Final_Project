import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://qa-admin.trado.co.il")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.driver.get("https://qa-admin.trado.co.il")

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()