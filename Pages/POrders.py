import allure
import pytest
from selenium.webdriver.common.keys import Keys

from Web.Locators.Home_Locators import HomeLocators
from selenium.webdriver.common.by import By
from time import sleep



class OrdersPage:

    def __init__(self,driver):
        self.driver = driver


