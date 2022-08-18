import requests


def post_add_new_pet(id_pet: int, name_pet: str):
    new_pet_data = {"id": id_pet, "category": {"id": 3, "name": "Psyduck"},
                    "name": name_pet, "photoUrls": ["string"],
                    "tags": [{"id": 0, "name": "string"}],
                    "status": "available"}

    response = requests.post(url='https://petstore.swagger.io/v2/pet', json=new_pet_data)
    assert response.status_code == 200
    f'Error! New pet doesnt add to store!, Actual status code {response.status_code} with error {response.json()}'


def get_add_new_pet(id_pet: int, name_pet: str):
    response = requests.get(url='https://petstore.swagger.io/v2/pet/3').json()
    print(response)
    if response['id'] == id_pet and response['name'] == name_pet:
        return True
    else:
        return False


def delete_new_pet(id_pet: int):
    response = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{id_pet}')
    assert response.status_code == 200
    f"Error! The pet has not been removed."
    f"Actual status code {response.status_code} with error {response.json()}"


def verify_del_new_pet(id_pet: int):
    response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{id_pet}')
    print(response.json())
    assert response.status_code == 404, \
        f"Error! Pet with id={id_pet} found!" \
        f"Actual status code {response.status_code} with error {response.json()}"
    if response.json()['message'] == 'Pet not found':
        return True
    else:
        return False


def post_new_user(id_user: int, name_user: str, f_name: str, l_name: str,
                  email: str, password: str, phone: str):
    global new_user_data
    new_user_data = {
        "id": id_user,
        "username": name_user,
        "firstName": f_name,
        "lastName": l_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": 3
    }
    response = requests.post(url='https://petstore.swagger.io/v2/user', json=new_user_data)
    assert response.status_code == 200
    f'Error! New user doesnt add to store!, Actual status code {response.status_code} with error {response.json()}'


def get_user(name_user: str):
    response = requests.get(f'https://petstore.swagger.io/v2/user/{name_user}')
    assert response.status_code == 200, \
        f"Error! User with username - {name_user} not found," \
        f"Actual status code {response.status_code} with error {response.json()}"
    print(response.json())


def put_user(id_user: int, name_user: str, f_name: str, l_name: str,
             email: str, password: str, phone: str):
    global put_data
    put_data = {
        "id": id_user,
        "username": name_user,
        "firstName": f_name,
        "lastName": l_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": 3
    }
    response = requests.put(url='https://petstore.swagger.io/v2/user/Rick', json=put_data)
    assert response.status_code == 200
    f'Error! User not found!, Actual status code {response.status_code} with error {response.json()}'


def verify_put_user(user_name: str):
    response = requests.get(url=f'https://petstore.swagger.io/v2/user/{user_name}')
    assert response.status_code == 200, \
        f"Error! User with username - {user_name} not found," \
        f"Actual status code {response.status_code} with error {response.json()}"
    print(response.json())
