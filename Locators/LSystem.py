#######    # system users page elements #     ##########
import self as self
from selenium.webdriver.common.by import By


class SystemElement:
    # element search users
    system_users_path = "//body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[24]/span[2]"

    phoneField = "//span[1]/div[1]/input[1]"

    phone = "1950000000"

    clickSend = "//form[1]/input[1]"

    passwordField = "//form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"

    password = "1234"

    clickLog = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"

    select_field = "//main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]"
    btn_system_users = "//span[contains(text(),'משתמשי מערכת')]"

    search_field = "//span[1]/span[1]/div[1]/input[1]"

    first_name_user = "//td[contains(text(),'סלמון')]"

    first_name_ = "סלמון"

    last_name_user = "//td[contains(text(),'טסמה')]"

    last_name_ = "טסמה"

    email_user = "//td[normalize-space()='gg@hh.com']"

    email_ = "gg@hh.com"

    phone_user = "//td[normalize-space()='0547877241']"

    phone_ = "0547877241"

    role_user = "//td[normalize-space()='owner']"

    role_ = "owner"

    authorization_user = "//th[contains(text(),'הרשאה')]"

    authorization_ = "write"

    authorization_2 = "הרשאה"

    stores_user = "//div[@class='paging_paging']"

    stores_ = "אדוניה סחר ושיווק"

    error_message = 'מציג\nלעמוד\nאין תוצאות\nסה״כ: 0 שורות'

    last_seen = "היום"

    creation_date = "16:"

    # element editing system user

    click_details = "(//td[normalize-space()='salmon@walla.com'])[1]"

    editing_firstname_user = "(//input[@placeholder='שם פרטי'])[1]"
    new_firstname = "סלמוןט"

    editing_lastname_user = "(//input[@placeholder='שם משפחה'])[1]"
    new_lastname = "סלמוןטט"

    editing_email_user = "(//input[@placeholder='דואר אלקטרוני'])[1]"
    new_email = "salmon@gmail.com"

    editing_phone_user = "(//input[@placeholder='טלפון'])[1]"
    new_phone = "11111"

    editing_role_user = "(//input[@placeholder='role'])[1]"
    index_roles = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/span[1]/div[2]/div[1]/div"


    editing_authorization_user = "(//input[@placeholder='הרשאה'])[1]"
    index_authorization = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[6]/div[1]/span"



    editing_stores_user = "(//input[@placeholder='חנויות'])[1]"
    new_store_name = ""

    btn_editing = "(//input[@value='עדכון'])[1]"


