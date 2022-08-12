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

    def verify_price_blue_duck(self):
        price_blue_duck = self.chrome.find_element(*CartPageLoc.price_blue_duck).text
        assert price_blue_duck == '14.52 €', 'Price is not correct'

    def verify_price_yellow_duck(self):
        price_yellow_duck = self.chrome.find_element(*CartPageLoc.price_yellow_duck).text
        assert price_yellow_duck == '13.07 €', 'Price is not correct'

    def verify_price_purple_duck(self):
        price_purple_duck = self.chrome.find_element(*CartPageLoc.price_purple_duck).text
        assert price_purple_duck == '0.00 €', 'Price is not correct'

    def verify_total_price(self):
        total_price = self.chrome.find_element(*CartPageLoc.total_price).text
        assert total_price == '27.59 €', 'Price is not correct'

    def order(self):
        order = self.chrome.find_element(*CartPageLoc.order)
        order.click()

    def verify_red_ducks_quantity(self):
        red_ducks_quantity = self.chrome.find_element(*CartPageLoc.red_ducks_quantity).text
        assert red_ducks_quantity == '3', 'Wrong number of ducks'

    def verify_total_price_for_3_ducks(self):
        total_price = self.chrome.find_element(*CartPageLoc.total_price_for_3_ducks).text
        assert total_price == total_price, 'Price is not correct'

    def remove(self):
        remove = self.chrome.find_element(*CartPageLoc.remove)
        remove.click()

    def verify_remove(self):
        veryfi_remove = self.chrome.find_element(*CartPageLoc.verify_remove).text
        assert veryfi_remove == 'There are no items in your cart.'
