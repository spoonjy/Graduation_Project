from LiteCart.Pages.base_page import BasePage
from LiteCart.Locators.edit_account_page_loc import EditAccountLoc

link = 'http://localhost/LiteCart/en/edit_account'


class EditAccountPage(BasePage):
    def edit_first_name(self):
        edit_first_name = self.chrome.find_element(*EditAccountLoc.edit_first_name)
        edit_first_name.clear()
        edit_first_name.send_keys('Ducks')

    def edit_last_name(self):
        edit_last_name = self.chrome.find_element(*EditAccountLoc.edit_last_name)
        edit_last_name.clear()
        edit_last_name.send_keys('Forever')

    def save(self):
        save = self.chrome.find_element(*EditAccountLoc.save)
        save.click()
