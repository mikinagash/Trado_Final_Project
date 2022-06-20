# from Web.Locators.Home_Locators import HomeLocators
from selenium.webdriver.common.by import By

from Locators.LSystem import SystemElement as EL
from time import sleep
import select
from selenium.webdriver.support.ui import Select



class SystemPage:

    def __init__(self, driver):
        self.driver = driver
        self.phoneField = EL.phoneField
        self.phone = EL.phone
        self.clickSend = EL.clickSend
        self.passwordField = EL.passwordField
        self.password = EL.password
        self.clickLog = EL.clickLog
        self.btn_serch = EL.btn_system_users
        self.serch_file = EL.search_field
        # self.clickDetails = EL.click_details
        self.firstname_user_editing = EL.editing_firstname_user
        self.lastname_user_editing = EL.editing_lastname_user
        self.email_user_editing = EL.editing_email_user
        self.phone_user_editing = EL.editing_phone_user
        self.role_user_editing = EL.editing_role_user
        self.authorization_user_editing = EL.editing_authorization_user
        self.stores_user_editing = EL.editing_stores_user
        self.clickBTN_editing = EL.btn_editing
        self.click_add_button = EL.click_Add_button
        self.click_add_ = EL.click_add
        self.click_user_detail = EL.click_detail_user


        # self.role_user_editing = EL.ad







    def Entrance(self):
        self.driver.find_element(By.XPATH, self.phoneField).send_keys(EL.phone)
        self.driver.find_element(By.XPATH, self.clickSend).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.passwordField).send_keys(EL.password)
        self.driver.find_element(By.XPATH, self.clickLog).click()
        self.driver.find_element(By.XPATH, self.btn_serch).click()


    # def Btn_serch(self):
    #     self.driver.find_element(By.XPATH, self.btn_serch).click()


    def click_serch_file(self):
        self.driver.find_element(By.XPATH, self.serch_file).click()

    def user_search(self, detail):
        self.driver.find_element(By.XPATH, self.serch_file).send_keys(detail)


    # editing system user
    # def clear_file(self,file):
    #     self.driver.find_element(By.XPATH, file).clear()


    def enter_id_user(self,detail):
        self.driver.find_element(By.XPATH, self.serch_file).click()
        self.driver.find_element(By.XPATH, self.serch_file).send_keys(detail)
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, self.click_user_detail).click()



    # def user_search(self, detail):
    #     self.driver.find_element(By.XPATH, self.serch_file).send_keys(detail)

    # def click_editing_system_user(self):
    #     self.driver.find_element(By.XPATH, self.clickDetails).click()

    def editing_firstname(self, name):
        self.driver.find_element(By.XPATH, self.firstname_user_editing).click()
        self.driver.find_element(By.XPATH, self.firstname_user_editing).clear()
        self.driver.find_element(By.XPATH, self.firstname_user_editing).send_keys(name)

    def editing_lastname(self,firsname):
        self.driver.find_element(By.XPATH, self.lastname_user_editing).click()
        self.driver.find_element(By.XPATH, self.lastname_user_editing).clear()
        self.driver.find_element(By.XPATH, self.lastname_user_editing).send_keys(firsname)

    def editing_email(self,email):
        self.driver.find_element(By.XPATH, self.email_user_editing).click()
        self.driver.find_element(By.XPATH, self.email_user_editing).clear()
        self.driver.find_element(By.XPATH, self.email_user_editing).send_keys(email)

    def editing_phone(self,phone):
        self.driver.find_element(By.XPATH, self.phone_user_editing).click()
        self.driver.find_element(By.XPATH, self.phone_user_editing).clear()
        self.driver.find_element(By.XPATH, self.phone_user_editing).send_keys(phone)

    def editing_role(self,num):
        self.driver.find_element(By.XPATH, self.role_user_editing).click()
        roles = self.driver.find_elements(By.XPATH, EL.index_roles)
        roles[num].click()

    def editing_authorization(self,num):
        self.driver.find_element(By.XPATH, self.authorization_user_editing).click()
        authorization = self.driver.find_elements(By.XPATH, EL.index_authorization)
        authorization[num].click()

    def editing_stores(self,store):
        self.driver.find_element(By.XPATH, self.stores_user_editing).click()
        self.driver.find_element(By.XPATH, self.stores_user_editing).clear()
        self.driver.find_element(By.XPATH, self.stores_user_editing).send_keys(store)
        # self.driver.find_element(By.XPATH, self.phone_user_editing).click()




    def editing_Btn_click(self):
        self.driver.find_element(By.XPATH, self.clickBTN_editing).click()

    def editing_error_messege_firstname(self):
        # self.driver.find_element(By.XPATH, self.clickBTN_editing).click()
        return self.driver.find_element(By.XPATH, self.firstname_user_editing).get_attribute('validationMessage')

    def editing_error_messege_lastname(self):
        return self.driver.find_element(By.XPATH, self.lastname_user_editing).get_attribute('validationMessage')

    def editing_error_messege_email(self):
        return self.driver.find_element(By.XPATH, self.email_user_editing).get_attribute('validationMessage')

    def editing_error_messege_stores(self):
        return self.driver.find_element(By.XPATH, self.stores_user_editing).get_attribute('validationMessage')

    def error_message_firstname(self):
        error_message_firstname = self.driver.find_element(By.XPATH, "//form[1]/div[1]/div[1]/div[1]").text
        assert error_message_firstname == 'נא למלא שדה זה'

    def error_message_lastname(self):
        error_message_lastname = self.driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[1]").text
        assert error_message_lastname == 'נא למלא שדה זה'

    def error_message_email(self):
        error_message_email = self.driver.find_element(By.XPATH, "//form[1]/div[1]/div[3]/div[1]").text
        assert error_message_email == 'נא למלא שדה זה'

    def error_message_email_invalid(self):
        # self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[3]/label[1]").click()
        error_message_email_invalid1 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]").text
        assert error_message_email_invalid1 == 'דוא"ל לא תקין'

    def error_message_phone_(self):
        error_message_phone_ = self.driver.find_element(By.XPATH, "//form[1]/div[1]/div[4]/div[1]").text
        assert error_message_phone_ == 'מס׳ טלפון לא תקין'

    def error_message_stores_(self):
        self.driver.find_element(By.XPATH, "//form[1]/div[1]/div[7]/label[1]").click()
        error_message_phone_ = self.driver.find_element(By.XPATH, "//form[1]/div[1]/div[7]/div[1]").text
        assert error_message_phone_ == 'נא למלא שדה זה'



    # def choose_role(self, num):
    #     roles = self.driver.find_elements(By.XPATH, EL.roles)
    #     roles[num].click()

#############
    def click_add_but(self):
        self.driver.find_element(By.XPATH, EL.click_Add_button).click()
        sleep(1)
        self.driver.find_element(By.XPATH, EL.click_add_user_).click()


    def click_add(self):
        self.driver.find_element(By.XPATH, EL.click_add).click()








