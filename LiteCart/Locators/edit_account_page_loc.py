from selenium.webdriver.common.by import By


class EditAccountLoc:
    edit_first_name = (By.XPATH, "//input[@name='firstname']")
    edit_last_name = (By.XPATH, "//input[@name='lastname']")
    save = (By.XPATH, "//button[@value='Save']")
