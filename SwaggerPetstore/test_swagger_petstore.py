import allure
from .swagger_petstore import *


class TestApiPetStore:
    @allure.story('Add new pet and delete from store')
    def test_pet(self):
        with allure.step('Adding new pet with id 3'):
            post_add_new_pet()
        with allure.step('Checking if a pet has been added with id 3'):
            get_add_new_pet()
        with allure.step('Removing pet with ID 3'):
            delete_new_pet()
        with allure.step('Checking remove pet with ID 3'):
            verify_del_new_pet()

    @allure.story('Create user, change first name and last name')
    def test_user(self):
        with allure.step('Creating new user'):
            post_new_user()
        with allure.step('Getting user data'):
            get_user()
        with allure.step('Changing username'):
            put_user()
        with allure.step('Getting user data after changed'):
            verify_put_user()
