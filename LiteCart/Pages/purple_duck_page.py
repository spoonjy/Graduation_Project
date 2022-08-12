import time

from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.purple_duck_page_loc import PurpleDuckLock
from LiteCart.Locators.main_page_loc import MainPageLoc

link = 'http://localhost/LiteCart/en/rubber-ducks-c-1/purple-duck-p-5'


class PurpleDuckPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.chrome.find_element(*PurpleDuckLock.add_to_cart)
        add_to_cart.click()

    def back_to_main_page(self):
        time.sleep(1)
        back_main_page = self.chrome.find_element(*MainPageLoc.back_main_page)
        back_main_page.click()
