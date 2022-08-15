from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.cart_page_loc import CartPageLoc

link = 'http://localhost/LiteCart/en/checkout'


class CartPage(BasePage):
    def verify_blue_duck_item(self):
        assert self.is_element_present(CartPageLoc.item_blue_duck), "Element is absent!"

    def verify_yellow_duck_item(self):
        assert self.is_element_present(CartPageLoc.item_yellow_duck), "Element is absent!"

    def verify_purple_duck_item(self):
        assert self.is_element_present(CartPageLoc.item_purple_duck), "Element is absent!"

    def verify_price_blue_duck(self, price: str):
        price_blue_duck = self.chrome.find_element(*CartPageLoc.price_blue_duck).text
        assert price_blue_duck == price
        f'Error: Incorrect price!, expected - {price}, actual - {price_blue_duck}'

    def verify_price_yellow_duck(self, price: str):
        price_yellow_duck = self.chrome.find_element(*CartPageLoc.price_yellow_duck).text
        assert price_yellow_duck == price
        f'Error: Incorrect price!, expected - {price}, actual - {price_yellow_duck}'

    def verify_price_purple_duck(self, price: str):
        price_purple_duck = self.chrome.find_element(*CartPageLoc.price_purple_duck).text
        assert price_purple_duck == price
        f'Error: Incorrect price!, expected - {price}, actual - {price_purple_duck}'

    def verify_total_price(self, t_price: str):
        total_price = self.chrome.find_element(*CartPageLoc.total_price).text
        assert total_price == t_price
        f'Error: Incorrect price!, expected - {t_price}, actual - {total_price}'

    def order(self):
        order = self.chrome.find_element(*CartPageLoc.order)
        order.click()

    def verify_red_ducks_quantity(self, quantity: str):
        red_ducks_quantity = self.chrome.find_element(*CartPageLoc.red_ducks_quantity).text
        assert red_ducks_quantity == quantity
        f'Error: Incorrect Quantity!, expected - {quantity}, actual - {red_ducks_quantity}'

    def verify_total_price_for_3_ducks(self, red_ducks_total_price: str):
        total_price = self.chrome.find_element(*CartPageLoc.total_price_for_3_ducks).text
        assert total_price == red_ducks_total_price
        f'Error: Incorrect price!, expected - {red_ducks_total_price}, actual - {total_price}'

    def remove(self):
        remove = self.chrome.find_element(*CartPageLoc.remove)
        remove.click()

    def verify_remove(self, text: str):
        veryfi_remove = self.chrome.find_element(*CartPageLoc.verify_remove).text
        assert veryfi_remove == text
        f'Error: Incorrect text, expected - {text}, actual - {veryfi_remove}'
