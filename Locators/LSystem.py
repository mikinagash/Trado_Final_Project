#######    # system users page elements #     ##########
# import self as self
from selenium.webdriver.common.by import By


class SystemElement:
    # element search users
    system_users_path = "//body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[24]/span[2]"

    id_user = "4jp555dl4b2tieg"
    click_detail_user = 'tbody tr:nth-child(1) td:nth-child(1)'

    phoneField = "//span[1]/div[1]/input[1]"

    phone = "1950000000"

    clickSend = "//form[1]/input[1]"

    passwordField = "//form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"

    password = "1234"

    clickLog = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"

    select_field = "//main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]"
    btn_system_users = "//span[contains(text(),'משתמשי מערכת')]"

    search_field = "//main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]"

    first_name_user = "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(1)"

    first_name_ = "ייהלם"

    last_name_user = "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(2)"

    last_name_ = "תהיי רצינית אושרת!"

    email_user = "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(3)"

    email_ = "doa2r@g2mail.com"

    phone_user = "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(4)"

    phone_ = "0556622938"

    role_user = "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(5)"

    role_ = "owner"

    authorization_user = "div.pages_pages main.pages_main div.pages_children div.table_tableScroll div.table_table table:nth-child(1) tbody:nth-child(2) tr:nth-child(1) > td:nth-child(6)"

    authorization_ = "write"

    authorization_2 = "הרשאה"

    stores_user = "//div[@class='paging_paging']"

    stores_ = "אדוניה סחר ושיווק"

    error_message = 'מציג\nלעמוד\nאין תוצאות\nסה״כ: 0 שורות'

    last_seen = "היום"

    creation_date = "16:"

    # element editing system user

    firstName_details = "//table[1]/tbody[1]/tr[1]/td[1]"

    lastName_details = "//table[1]/tbody[1]/tr[1]/td[2]"######################################################################

    email_details = "//table[1]/tbody[1]/tr[1]/td[3]"

    phone_details = "//table[1]/tbody[1]/tr[1]/td[4]"

    role_details = "//table[1]/tbody[1]/tr[1]/td[5]"

    authorization_details = "//table[1]/tbody[1]/tr[1]/td[6]"

    editing_firstname_user = "//input[@placeholder='שם פרטי']"
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
    index_authorization = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[6]/div[1]/span[1]/div[2]/div[1]/div"



    editing_stores_user = "(//input[@placeholder='חנויות'])[1]"
    new_store_name = "סלמון ובניו"

    btn_editing = "//form[1]/input[1]"

    new_user_edition = "(//td[contains(text(),'סלמוןט')])[1]"

###############
    click_Add_button = "//main[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]"
    click_add_user_ = "//span[contains(text(),'הוספה')]"
    click_add = "//form[1]/input[1]"
    lin_add_user = "//tbody/tr[1]/td[1]"
    error_message_pops_up = 'זהו שדה חובה.'
