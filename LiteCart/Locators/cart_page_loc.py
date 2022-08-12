from selenium.webdriver.common.by import By


class CartPageLoc:
    item_blue_duck = (By.XPATH, "//td[@class='item'][text()='Blue Duck']")
    item_yellow_duck = (By.XPATH, "//td[@class='item'][text()='Yellow Duck']")
    item_purple_duck = (By.XPATH, "//td[@class='item'][text()='Purple Duck']")
    item_red_duck = (By.XPATH, "//td[@class='item'][text()='Red Duck']")

    price_blue_duck = (By.XPATH, "//td[@class='unit-cost'][text()='14.52 €']")
    price_yellow_duck = (By.XPATH, "//td[@class='unit-cost'][text()='13.07 €']")
    price_purple_duck = (By.XPATH, "//td[@class='unit-cost'][text()='0.00 €']")

    total_price = (By.XPATH, "//td[text()='27.59 €']")

    order = (By.XPATH, "//button[@name='confirm_order']")
    red_ducks_quantity = (By.XPATH, "//td[@style='text-align: center;'][text()='3']")
    total_price_for_3_ducks = (By.XPATH, "//td[@class='sum']")
    remove = (By.XPATH, "//button[@value='Remove']")
    verify_remove = (By.XPATH, "//*[text()='There are no items in your cart.']")
