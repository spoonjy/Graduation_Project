import time

from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.red_duck_page_loc import RedDuckLock
from LiteCart.Locators.main_page_loc import MainPageLoc

link = 'http://localhost/LiteCart/en/rubber-ducks-c-1/red-duck-p-3'


class RedDuckPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.chrome.find_element(*RedDuckLock.add_to_cart)
        add_to_cart.click()

    def back_to_main_page(self):
        back_main_page = self.chrome.find_element(*MainPageLoc.back_main_page)
        back_main_page.click()

    def quantity(self, red_quantity: str):
        quantity = self.chrome.find_element(*RedDuckLock.edit_quantity)
        quantity.clear()
        quantity.send_keys(red_quantity)

    def go_cart(self):
        time.sleep(1)
        go_cart = self.chrome.find_element(*MainPageLoc.go_cart)
        go_cart.click()
