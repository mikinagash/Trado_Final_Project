
class LocatorsStores:
    ##login locators
    phoneField = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    phone = "1950000000"
    clickSend = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"
    passwordField = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    password = "1234"
    clickLog = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"
    #add/update store locators
    addButton= "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]"
    adding = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]"
    bnNumField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    nameField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/div[1]/input[1]"
    websiteField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/div[1]/input[1]"
    descriptionField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[4]/span[1]/div[1]/input[1]"
    telephoneField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[7]/span[1]/div[1]/input[1]"
    emailField="//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[8]/span[1]/div[1]/input[1]"
    departmentField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[9]/span[1]/div[2]/input[1]"
    selectDepart= "//div[contains(text(),'fdgfd')]"
    cityField ="//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/div[1]/span[1]/div[1]/input[1]"
    streetField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/div[2]/span[1]/div[1]/input[1]"
    buildingField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/div[3]/span[1]/div[1]/input[1]"
    apartmentField= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/div[4]/span[1]/div[1]/input[1]"
    addStoreButton= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/input[1]"
    ##search store locators
    searchStorefield= "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]"
    ##update store details
    storeName= "//tbody/tr[1]/td[2]"
    updateButton= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/input[1]"
    ##assert deatails in table
    assEmail= "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(2)"
    assName= "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(2)"
    assBnNum= "//tbody/tr[5]/td[1]"
    assPhone="//tbody/tr[2]/td[4]"
    assAddress= "//tbody/tr[1]/td[7]"
    ##assert fields
    assError= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]"
    assErrorCity= "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/div[1]/div[1]"
    assErrorEmail= "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[8]/div[1]"
    assErrorPhone= "//div[contains(text(),'מס׳ טלפון לא תקין')]"
    ##upload photo
    logoField= "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/input[1]"
    logoPath= r'//Users/racha/Downloads/logoweb.jpg'




