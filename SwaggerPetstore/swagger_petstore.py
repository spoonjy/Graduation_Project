import requests


def post_add_new_pet():
    new_pet_data = {"id": 3, "category": {"id": 3, "name": "Psyduck"},
                    "name": "duck", "photoUrls": ["string"],
                    "tags": [{"id": 0, "name": "string"}],
                    "status": "available"}

    response = requests.post(url='https://petstore.swagger.io/v2/pet', json=new_pet_data)
    return response


def get_add_new_pet():
    response = requests.get(url='https://petstore.swagger.io/v2/pet/3').json()
    print(response)
    if response['id'] == 3 and response['name'] == 'duck':
        return True
    else:
        return False


def delete_new_pet():
    response = requests.delete(url='https://petstore.swagger.io/v2/pet/3').json()
    return response


def verify_del_new_pet():
    response = requests.get(url='https://petstore.swagger.io/v2/pet/3').json()
    print(response)
    if response['message'] == 'Pet not found':
        return True
    else:
        return False


def post_new_user():
    global new_user_data
    new_user_data = {
        "id": 3,
        "username": "Rick",
        "firstName": "Yaroslav",
        "lastName": "Lukashevich",
        "email": "Yar@gmail.com",
        "password": "123321",
        "phone": "+375331234567",
        "userStatus": 3
    }
    response = requests.post(url='https://petstore.swagger.io/v2/user', json=new_user_data)
    return response


def get_user():
    response = requests.get('https://petstore.swagger.io/v2/user/Rick').json()
    assert new_user_data == response, 'User not found'
    print(response)


def put_user():
    global put_data
    put_data = {
        "id": 3,
        "username": "Ducker",
        "firstName": "Yaroslav",
        "lastName": "Lukashevich",
        "email": "Yar@gmail.com",
        "password": "123321",
        "phone": "+375331234567",
        "userStatus": 3
    }
    response = requests.put(url='https://petstore.swagger.io/v2/user/Rick', json=put_data)
    return response


def verify_put_user():
    response = requests.get(url='https://petstore.swagger.io/v2/user/Ducker').json()
    assert put_data == response, 'User not found'
    print(response)
