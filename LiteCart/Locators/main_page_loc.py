from selenium.webdriver.common.by import By


class MainPageLoc:
    change_loc = (By.XPATH, "//div[@class = 'change']")
    change_currency_loc = (By.XPATH, "//select[@name = 'currency_code']")
    change_currency_loc_EUR = (By.XPATH, "//select/option[@value = 'EUR']")
    change_country_loc = (By.XPATH, "//select[@name = 'country_code']")
    change_country_loc_PL = (By.XPATH, "//select/option[@value = 'PL']")
    save = (By.XPATH, "//button[@value = 'Save']")

    verify_currency = (By.XPATH, "//div[@class = 'currency']/span ['EUR']")
    verify_country = (By.XPATH, "//div[@title = 'Poland']")

    email_loc = (By.XPATH, "//input[@name = 'email']")
    pass_loc = (By.XPATH, "//input[@name = 'password']")
    login_loc = (By.XPATH, "//button[@name = 'login']")

    purple_duck = (By.XPATH, "//div[@id='box-most-popular']//img[@alt='Purple Duck']")
    red_duck = (By.XPATH, "//div[@id='box-most-popular']//img[@alt='Red Duck']")
    blue_duck = (By.XPATH, "//div[@id='box-most-popular']//img[@alt='Blue Duck']")
    yellow_duck = (By.XPATH, "//div[@id='box-most-popular']//img[@alt='Yellow Duck']")

    back_main_page = (By.XPATH, "//img[@title='My Store']")
    go_cart = (By.XPATH, "//div[@id='cart']")

    edit_account = (By.XPATH, "//div[@id='box-account']//a[text()='Edit Account']")
