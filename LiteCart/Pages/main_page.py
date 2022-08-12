import time

from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.main_page_loc import MainPageLoc

link = 'http://localhost/LiteCart/en/'


class LiteCartMainPage(BasePage):
    def change_currency(self):
        change_currency = self.chrome.find_element(*MainPageLoc.change_loc)
        change_currency.click()
        change_currency_select = self.chrome.find_element(*MainPageLoc.change_currency_loc)
        change_currency_select.click()
        change_currency_select_eur = self.chrome.find_element(*MainPageLoc.change_currency_loc_EUR)
        change_currency_select_eur.click()

    def change_country(self):
        change_country = self.chrome.find_element(*MainPageLoc.change_country_loc)
        change_country.click()
        change_country_pl = self.chrome.find_element(*MainPageLoc.change_country_loc_PL)
        change_country_pl.click()

    def save_button(self):
        save_button = self.chrome.find_element(*MainPageLoc.save)
        save_button.click()

    def verify_currency(self):
        verify_currency = self.chrome.find_element(*MainPageLoc.verify_currency).text
        assert verify_currency == 'EUR', 'Currency is not EUR'

    def verify_country(self):
        verify_county = self.chrome.find_element(*MainPageLoc.verify_country).text
        assert verify_county == 'Poland', 'Country is not Poland'

    def login(self):
        email = self.chrome.find_element(*MainPageLoc.email_loc)
        email.send_keys('Yar@gmail.com')
        password = self.chrome.find_element(*MainPageLoc.pass_loc)
        password.send_keys('admin')
        login = self.chrome.find_element(*MainPageLoc.login_loc)
        login.click()

    def purple_duck(self):
        purple_duck = self.chrome.find_element(*MainPageLoc.purple_duck)
        purple_duck.click()

    def red_duck(self):
        red_duck = self.chrome.find_element(*MainPageLoc.red_duck)
        red_duck.click()

    def blue_duck(self):
        blue_duck = self.chrome.find_element(*MainPageLoc.blue_duck)
        blue_duck.click()

    def yellow_duck(self):
        yellow_duck = self.chrome.find_element(*MainPageLoc.yellow_duck)
        yellow_duck.click()

    def go_cart(self):
        time.sleep(1)
        go_cart = self.chrome.find_element(*MainPageLoc.go_cart)
        go_cart.click()

    def edit_account(self):
        edit_account = self.chrome.find_element(*MainPageLoc.edit_account)
        edit_account.click()
