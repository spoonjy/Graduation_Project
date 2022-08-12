import time

from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.yellow_duck_loc import YellowDuckLock
from LiteCart.Locators.main_page_loc import MainPageLoc

link = 'http://localhost/LiteCart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1'


class YellowDuckPage(BasePage):
    def size(self):
        size = self.chrome.find_element(*YellowDuckLock.size)
        size.click()

    def add_to_cart(self):
        add_to_cart = self.chrome.find_element(*YellowDuckLock.add_to_cart)
        add_to_cart.click()

    def back_to_main_page(self):
        time.sleep(1)
        back_main_page = self.chrome.find_element(*MainPageLoc.back_main_page)
        back_main_page.click()
