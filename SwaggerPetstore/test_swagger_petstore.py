import allure
from .swagger_petstore import *


class TestApiPetStore:
    @allure.story('Add new pet and delete from store')
    def test_add__pet_and_delete_pet_from_store(self):
        with allure.step('Adding new pet with id 3'):
            post_add_new_pet(3, 'duck')
        with allure.step('Checking if a pet has been added with id 3'):
            get_add_new_pet(3, 'duck')
        with allure.step('Removing pet with ID 3'):
            delete_new_pet(3)
        with allure.step('Checking remove pet with ID 3'):
            verify_del_new_pet(3)

    @allure.story('Create user, change first name and last name')
    def test_add_user_and_change_his_first_name_and_last_name(self):
        with allure.step('Creating new user'):
            post_new_user(3, "Rick", "Yaroslav", "Lukashevich", "Yar@gmail.com", "123321", "+375331234567")
        with allure.step('Getting user data'):
            get_user('Rick')
        with allure.step('Changing username'):
            put_user(3, "Ducker", "Yaroslav", "Lukashevich", "Yar@gmail.com", "123321", "+375331234567")
        with allure.step('Getting user data after changed'):
            verify_put_user('Ducker')
