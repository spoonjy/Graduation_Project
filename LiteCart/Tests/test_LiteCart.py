import pytest
import allure
from selenium import webdriver
from LiteCart.db_litecart import *
from webdriver_manager.chrome import ChromeDriverManager
from LiteCart.Pages.main_page import LiteCartMainPage
from LiteCart.Pages.purple_duck_page import PurpleDuckPage
from LiteCart.Pages.blue_duck_page import BlueDuckPage
from LiteCart.Pages.yellow_dock_page import YellowDuckPage
from LiteCart.Pages.red_duck_page import RedDuckPage
from LiteCart.Pages.cart_page import CartPage
from LiteCart.Pages.edit_account_page import EditAccountPage


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@allure.story('Currency and country change')
def test_change_currency_and_country_verify_change(open_browser):
    link = 'http://localhost/LiteCart/en/'

    with allure.step('Opening Lite Cart main page'):
        lite_cart_page = LiteCartMainPage(browser, link)
        lite_cart_page.open()

    with allure.step('Changing currency'):
        lite_cart_page.change_currency()
    with allure.step('Changing country'):
        lite_cart_page.change_country()
    with allure.step('Click save button'):
        lite_cart_page.save_button()

    with allure.step('Checking change currency'):
        lite_cart_page.verify_currency('EUR')
    with allure.step('Checking change country'):
        lite_cart_page.verify_country('Poland')


@allure.story('Log in, added ducks to cart and order ducks')
def test_added_ducks_to_cart_verify_added_and_price_order(open_browser):
    link = 'http://localhost/LiteCart/en/'

    with allure.step('Opening Lite Cart main page'):
        lite_cart_page = LiteCartMainPage(browser, link)
        lite_cart_page.open()

    with allure.step('Log in'):
        lite_cart_page.login('Yar@gmail.com', 'admin')
    with allure.step('Changing currency'):
        lite_cart_page.change_currency()
    with allure.step('Changing country'):
        lite_cart_page.change_country()
    with allure.step('Click save button'):
        lite_cart_page.save_button()

    with allure.step('Opening purple duck page'):
        lite_cart_page.purple_duck()
        purple_duck_page = PurpleDuckPage(browser, url=browser.current_url)
    with allure.step('Adding purple duck to cart'):
        purple_duck_page.add_to_cart()
    with allure.step('Go back to main page'):
        purple_duck_page.back_to_main_page()

    with allure.step('Opening blue duck page'):
        lite_cart_page.blue_duck()
        blue_duck_page = BlueDuckPage(browser, url=browser.current_url)
    with allure.step('Adding blue duck to cart'):
        blue_duck_page.add_to_cart()
    with allure.step('Go back to main page'):
        blue_duck_page.back_to_main_page()

    with allure.step('Opening yellow duck page'):
        lite_cart_page.yellow_duck()
        yellow_duck_page = YellowDuckPage(browser, url=browser.current_url)
    with allure.step('Choosing a size'):
        yellow_duck_page.size()
    with allure.step('Adding yellow duck to cart'):
        yellow_duck_page.add_to_cart()
    with allure.step('Go back to main page'):
        yellow_duck_page.back_to_main_page()

    with allure.step('Opening cart page'):
        lite_cart_page.go_cart()
        cart_page = CartPage(browser, url=browser.current_url)
    with allure.step('Checking for the presence of a blue duck in cart'):
        cart_page.verify_blue_duck_item()
    with allure.step('Checking for the presence of a yellow duck in cart'):
        cart_page.verify_yellow_duck_item()
    with allure.step('Checking for the presence of a purple duck in cart'):
        cart_page.verify_purple_duck_item()

    with allure.step('Blue duck price checking'):
        cart_page.verify_price_blue_duck('14.52 €')
    with allure.step('Yellow duck price checking'):
        cart_page.verify_price_yellow_duck('13.07 €')
    with allure.step('Purple duck price checking'):
        cart_page.verify_price_purple_duck('0.00 €')
    with allure.step('Total price checking'):
        cart_page.verify_total_price('27.59 €')

    with allure.step('Confirm order'):
        cart_page.order()
    with allure.step('Checking order in db'):
        verify_order_in_db()


@allure.story('Log in and edit user')
def test_login_and_edit_name_verify_edit(open_browser):
    link = 'http://localhost/LiteCart/en/'

    with allure.step('Opening Lite Cart main page'):
        lite_cart_page = LiteCartMainPage(browser, link)
        lite_cart_page.open()
    with allure.step('Log in'):
        lite_cart_page.login('Yar@gmail.com', 'admin')

    with allure.step('Opening edit page'):
        lite_cart_page.edit_account()
        edit_account_page = EditAccountPage(browser, url=browser.current_url)
    with allure.step('Editing firs name'):
        edit_account_page.edit_first_name('Ducks')
    with allure.step('Editing last name'):
        edit_account_page.edit_last_name('Forever')
    with allure.step('Click save'):
        edit_account_page.save()

    with allure.step('Checking changes first name in db'):
        verify_edit_first_name_in_db('Ducks')
    with allure.step('Checking changes last name in db'):
        verify_edit_last_name_in_db('Forever')


@allure.story('Checking removal of a duck from the cart after it has been added there')
def test_added_duck_to_cart_remove_verify_remove(open_browser):
    link = 'http://localhost/LiteCart/en/'

    with allure.step('Opening Lite Cart main page'):
        lite_cart_page = LiteCartMainPage(browser, link)
        lite_cart_page.open()

    with allure.step('Changing currency'):
        lite_cart_page.change_currency()
    with allure.step('Click save'):
        lite_cart_page.save_button()

    with allure.step('Opening red duck page'):
        lite_cart_page.red_duck()
        red_duck_page = RedDuckPage(browser, url=browser.current_url)
    with allure.step('Changing quantity ducks'):
        red_duck_page.quantity('3')
    with allure.step('Adding red duck to cart'):
        red_duck_page.add_to_cart()

    with allure.step('Opening cart page'):
        red_duck_page.go_cart()
        cart_page = CartPage(browser, url=browser.current_url)
    with allure.step('Quantity duck checking'):
        cart_page.verify_red_ducks_quantity('3')

    with allure.step('Total price checking'):
        cart_page.verify_total_price_for_3_ducks('43.56 €')

    with allure.step('Removing ducks from cart'):
        cart_page.remove()
    with allure.step('Checking empty cart'):
        cart_page.verify_remove('There are no items in your cart.')
