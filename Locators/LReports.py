class Reports:

    # login locators:
    phoneField = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    phone = "1950000000"
    clickSend = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"
    passwordField = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    password = "1234"

    # reports locators
    reportsPageButton = "//span[contains(text(),'Reports')]"
    datesbutton = "//div[@id='date_displey']"
    saveButton = "//button[contains(text(),'שמירה')]"

    # containn 2 elements
    ltwofields = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span"
    # contain 6 elements - today/yesterday/currentweek/previuosweek/currentmonth/previousmonth
    lrdrStaticRange = "//body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button"
    # contain 35 elements
    lrdrDays = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/button"

    # ui locators
    tradologo = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[1]/div[1]/a[1]/img[1]"
    reportsh4logo = "//h4[contains(text(),'Reports')]"
    barsicon = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[1]/div[1]/span[1]/span[1]/i[1]"
    imglink ="https://storage.cloud.google.com/trado_images/settings/value-2rnvbaw5joki7qm8ud?1607509995191"

    # buttons left and right on the calendar
    datesLeftButton = "//body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]/i[1]"
    datesRightButton = "//body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/button[2]/i[1]"


    # left and right  selected dates
    datesLeftselected = "//body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/input[1]"
    dateRightselected = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/input[1]"

    # left months scroll down
    leftscroldown = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/span[1]/select[1]"
    # right months scroll down
    righhtscroldown = "//body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/span[3]/select[1]"





    #=##==#= system ui
    # עמוד משתמשים
    systemuserspage = "//span[contains(text(),'משתמשי מערכת')]"
    #  צד ימין למעלה לוגו עם שם דף
    systemh4logotext = "//h4[contains(text(),'משתמשי מערכת')]"
    # לחצן עם  שלוש מלבנים צד ימין למעלה
    barsiconsystem = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[1]/div[1]/span[1]/span[1]/i[1]"
    # שדה חיפוש
    serchfieldsystem = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/span[1]"
    # טבלה של פרטים
    details_table = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]"