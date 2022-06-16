from Locators.LStores import LocatorsStores
from selenium.webdriver.common.by import By
from time import sleep
from random import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StoresPage(LocatorsStores):

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.XPATH, self.phoneField).send_keys(self.phone)
        sleep(2)
        self.driver.find_element(By.XPATH, self.clickSend).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.passwordField).send_keys(self.password)
        sleep(2)
        self.driver.find_element(By.XPATH, self.clickLog).click()
        sleep(2)
        self.driver.get("https://qa-admin.trado.co.il/#/stores")
        self.addButton= LocatorsStores.addButton
        self.adding=LocatorsStores.adding
        self.bnNumField=LocatorsStores.bnNumField
        self.nameField=LocatorsStores.nameField
        self.websiteField=LocatorsStores.websiteField
        self.descriptionField=LocatorsStores.descriptionField
        self.telephoneField=LocatorsStores.telephoneField
        self.emailField=LocatorsStores.emailField
        self.departmentField=LocatorsStores.departmentField
        self.cityField= LocatorsStores.cityField
        self.streetField=LocatorsStores.streetField
        self.buildingField=LocatorsStores.buildingField
        self.apartmentField=LocatorsStores.apartmentField
        self.addStoreButton=LocatorsStores.addStoreButton
        ##search
        self.searchStorefield=LocatorsStores.searchStorefield


    def click_add_buttonn(self):
        self.driver.find_element(By.XPATH, self.addButton).click()

    def click_adding(self):
        self.driver.find_element(By.XPATH, self.adding).click()

    def enter_bnNumber(self):
        self.bnNum= randint(100,10000000000)
        self.driver.find_element(By.XPATH, self.bnNumField).send_keys(self.bnNum)

    #required field
    def enter_storeName(self,name):
        self.driver.find_element(By.XPATH, self.nameField).send_keys(name)

    def enter_websiteUrl(self,url):
        self.driver.find_element(By.XPATH, self.websiteField).send_keys(url)

    def enter_description(self,des):
        self.driver.find_element(By.XPATH, self.descriptionField).send_keys(des)

    def enter_storePhone(self,phoneNum):
        self.driver.find_element(By.XPATH, self.telephoneField).send_keys(phoneNum)

    def enter_storeEmail(self,email):
        self.driver.find_element(By.XPATH, self.emailField).send_keys(email)

    def enter_storeDepartment(self,depart):
        self.driver.find_element(By.XPATH, self.departmentField).send_keys(depart)
        # # self.driver.find_element(By.XPATH,self.departmentField).click()
        # select = Select(self.driver.find_element(By.XPATH, self.departmentField))
        # select.select_by_visible_text(depart)


    # required field
    def enter_storeCity(self,city):
        self.driver.find_element(By.XPATH, self.cityField).send_keys(city)

    # required field
    def enter_storeStreet(self,street):
        self.driver.find_element(By.XPATH, self.streetField).send_keys(street)

    # required field
    def enter_storeBuilding(self,buildNum):
        self.driver.find_element(By.XPATH, self.buildingField).send_keys(buildNum)

    def enter_storeApartment(self,apt):
        self.driver.find_element(By.XPATH, self.apartmentField).send_keys(apt)

    def click_addNewStore(self):
        self.driver.find_element(By.XPATH, self.addStoreButton).click()


##search stores functions

    def search_store(self,details):
        self.driver.find_element(By.XPATH,self.searchStorefield).send_keys(details)





