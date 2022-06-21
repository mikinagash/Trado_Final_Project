from Locators.LStores import LocatorsStores
from selenium.webdriver.common.by import By
from time import sleep
from random import *


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
        self.logoField=LocatorsStores.logoField
        self.logoPath=LocatorsStores.logoPath
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
        ##update
        self.storeName=LocatorsStores.storeName
        self.updateButton=LocatorsStores.updateButton
        ##assert
        self.assName=LocatorsStores.assName
        self.assAddress=LocatorsStores.assAddress
        self.assEmail=LocatorsStores.assEmail
        self.assBnNum=LocatorsStores.assBnNum
        self.assPhone=LocatorsStores.assPhone
        self.assError=LocatorsStores.assError
        self.assErrorCity=LocatorsStores.assErrorCity
        self.assErrorEmail=LocatorsStores.assErrorEmail
        self.assErrorPhone=LocatorsStores.assErrorPhone
        self.assNoResults=LocatorsStores.assNoResults
        self.assDuplicate=LocatorsStores.assDuplicate
        self.tradologo=LocatorsStores.tradologo

    def add_store(self):
        self.driver.find_element(By.XPATH, self.addButton).click()
        self.driver.find_element(By.XPATH, self.adding).click()


    def click_on_feild(self):
       self.driver.find_element(By.XPATH, self.nameField).click()

    def add_store_form_optionalFields(self,url,des,phoneNum,email,apt):
        self.bnNum = randint(100, 10000000000)
        self.driver.find_element(By.XPATH, self.bnNumField).send_keys(self.bnNum)
        self.driver.find_element(By.XPATH, self.websiteField).send_keys(url)
        self.driver.find_element(By.XPATH, self.descriptionField).send_keys(des)
        self.driver.find_element(By.XPATH, self.telephoneField).send_keys(phoneNum)
        self.driver.find_element(By.XPATH, self.emailField).send_keys(email)
        self.driver.find_element(By.XPATH, self.apartmentField).send_keys(apt)

    def department(self, num):
        self.driver.find_element(By.XPATH, self.departmentField).click()
        depart = self.driver.find_elements(By.XPATH, self.selectDepart)
        depart[num].click()


    def add_store_form_requiredFields(self,name,city,street,buildNum):
        self.driver.find_element(By.XPATH, self.nameField).send_keys(name)
        self.driver.find_element(By.XPATH, self.cityField).send_keys(city)
        self.driver.find_element(By.XPATH, self.streetField).send_keys(street)
        self.driver.find_element(By.XPATH, self.buildingField).send_keys(buildNum)

    def clear_required_fields(self):
        self.driver.find_element(By.XPATH, self.nameField).clear()
        self.driver.find_element(By.XPATH, self.cityField).clear()
        self.driver.find_element(By.XPATH, self.streetField).clear()
        self.driver.find_element(By.XPATH, self.buildingField).clear()

    def clear_optional_fields(self):
        self.driver.find_element(By.XPATH, self.bnNumField).clear()
        self.driver.find_element(By.XPATH, self.websiteField).clear()
        self.driver.find_element(By.XPATH, self.descriptionField).clear()
        self.driver.find_element(By.XPATH, self.telephoneField).clear()
        self.driver.find_element(By.XPATH, self.emailField).clear()
        self.driver.find_element(By.XPATH, self.departmentField).clear()
        self.driver.find_element(By.XPATH, self.apartmentField).clear()


    def click_addNewStore(self):
        self.driver.find_element(By.XPATH, self.addStoreButton).click()

##search stores functions

    def search_store(self,details):
        self.driver.find_element(By.XPATH,self.searchStorefield).send_keys(details)

##update store deatils

    def click_on_store_name(self):
        self.driver.find_element(By.CSS_SELECTOR,self.storeName).click()

    def click_update(self):
        self.driver.find_element(By.XPATH,self.updateButton).click()

    ##assert functions

    def verify_By_text(self,elmnt):
        x = self.driver.find_element(By.CSS_SELECTOR, elmnt).text
        return x


    def verify_by_innerText(self,elmnt):
        x = self.driver.find_element(By.XPATH, elmnt).get_attribute("innerText")
        return x

    def verify_NoResults(self):
        x= self.driver.find_element(By.XPATH,self.assNoResults).text
        return x





######## ui #######

    def trado_logo_1(self):
        value = self.driver.find_element(By.XPATH,self.tradologo).get_attribute("src")
        return value


    def store_h4_logo_stores(self):
        value = self.driver.find_element(By.XPATH,self.storeh4logotext).get_attribute("innerHTML")
        Height = self.driver.find_element(By.XPATH, self.storeh4logotext).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.storeh4logotext).get_attribute("clientWidth")
        return value ,Height ,Width



    def bars_icon_store(self):
        Height = self.driver.find_element(By.XPATH, self.barsicon).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.barsicon).get_attribute("clientWidth")
        return Height , Width


    def search_field_size(self):
        Height = self.driver.find_element(By.XPATH, self.search_field_stores).get_attribute("clientHeight")
        Width = self.driver.find_element(By.XPATH, self.search_field_stores).get_attribute("clientWidth")
        return Height, Width




