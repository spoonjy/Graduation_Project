from selenium.webdriver.common.by import By


class RedDuckLock:
    add_to_cart = (By.XPATH, "//button[@name='add_cart_product']")
    edit_quantity = (By.XPATH, "//input[@name='quantity']")
