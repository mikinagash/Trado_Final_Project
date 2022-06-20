class OrdersElement:
# connect element

    phoneField = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    phone = "1950000000"
    clickSend = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"
    passwordField = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    password = "1234"
    clickLog = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"

# orders page elements rivka
    order_path = "//tbody/tr[2]/td[2]"
    click_search = "(//input[@placeholder='חיפוש בהזמנות'])[1]"
    search = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]"
    switch_page = "//span[contains(text(),'2')]"
    ready_order = "//span[contains(text(),'מוכנה')]"
    delivery_order = "//span[contains(text(),'במשלוח')]"
    end_page = "//span[contains(text(),'סיום')]"
    clicking_on_a_column = "//tbody/tr[1]/td[6]"
    quantity = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/span[1]/div[1]/input[1]"
    select_quantity = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/span[1]/div[2]/div[1]/div[2]"
    # index_quantity = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/span[1]/div[2]/div[1]/div"
    pallets= "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/span[1]/div[1]/input[1]"
    select_pallets = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/span[1]/div[2]/div[1]/div[8]"
    ready_to_delivery = "//button[contains(text(),'סמן הזמנה כמוכנה למשלוח')]"
    on_delivery = "//button[contains(text(),'סמן הזמנה כנשלחה')]"
    Reached_destination = "//button[contains(text(),'ההזמנה הגיעה ליעדה')]"
    weight = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/input[1]"
    wgt = "10000"
    enter_to_order_page = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[5]/span[2]"
    Missing_product = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]"
    change_product = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]"
    change_product_windows ="/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h4[1]"
    # aseert
    pyType = "//tbody/tr[1]/td[11]"
    no_result = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]"
    switch = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]"
    order_ready = "//tbody/tr[1]/td[2]"
    change_product_ = "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h4[1]"
    order_num_search = "//tbody/tr/td[1]"
    Dis_details = "//span[contains(text(),'מספר הזמנה: 487')]"
    id = "1e1xpmlil4dzq0jn"
    new_status = "//div[contains(text(),'סטטוס הזמנה עודכן בהצלחה')]"
    pallets_status="//div[contains(text(),'סטטוס משטחים עודכן בהצלחה')]"

    # ui
    logo = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/a[1]/img[1]"
    orders = "//h4[contains(text(),'הזמנות')]"
    orders_status = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]"
    search_from_orders = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]"
    up_table = "//thead//tr"






