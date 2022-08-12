import time
from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.blue_duck_page_loc import BlueDuckLock
from LiteCart.Locators.main_page_loc import MainPageLoc

link = 'http://localhost/LiteCart/en/rubber-ducks-c-1/blue-duck-p-4'


class BlueDuckPage(BasePage):
    def add_to_cart(self):
        add_to_cart = self.chrome.find_element(*BlueDuckLock.add_to_cart)
        add_to_cart.click()

    def back_to_main_page(self):
        time.sleep(1)
        back_main_page = self.chrome.find_element(*MainPageLoc.back_main_page)
        back_main_page.click()
