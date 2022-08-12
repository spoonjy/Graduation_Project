from selenium.webdriver.common.by import By


class YellowDuckLock:
    add_to_cart = (By.XPATH, "//button[@name='add_cart_product']")
    size = (By.XPATH, "//select[@name='options[Size]']//option[@value='Small']")
