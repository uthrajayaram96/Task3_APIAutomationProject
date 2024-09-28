"""
Test Plan:
1. Get a list of items/records/users  - test_get_users() -> json payload, response_code = 200 (success)
2. Get a user/record - test_get_an_user() -> json payload, response_code = 200
3. Create a user - test_create_user() , response_code = 201
4. Update a user - test_update_user(), response_code = 200
5. Delete user - test_delete_user(), response_code = 204
6. Register user - test_register_success(), response_code = 200
7. Register user  - test_register_not_success(), response_code = 400
8. Login user - test_login_success(), response_code = 200
9. Login user  - test_login_not_success(), response_code = 400

"""
import requests
import json

base_url = "https://reqres.in/api"


# helper function to print the response
def print_response(response):
    st_code = response.status_code
    print(f"Response code : {st_code}")
    if st_code == 204:
        print("Response body : { }")
    else:
        print(f"Response body : {response.json()}")


# Test Case 1: - Test if we can get list of all users, response_code = 200
def test_get_users():
    url = f"{base_url}/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200, f"Response_code received = {response.status_code} but expected 200!"

    print('Test case 1 passed!')
    print_response(response)


# Test Case 2: Test if we can get a user.
def test_get_a_user(user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)

    assert response.status_code == 200, f"Response_code received = {response.status_code} but expected 200!"

    print('Test case 2 passed!')
    print_response(response)


# Test Case 3: Test if we can create a user
def test_create_user():
    url = f"{base_url}/users"
    request_payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url, json=request_payload)

    assert response.status_code == 201, f"Response_code received = {response.status_code} but expected 201!"

    print('Test case 3 passed!')
    print_response(response)


# Test Case 4: Test if we can update the user
def test_update_user():
    url = f"{base_url}/users/2"
    request_payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(url, json=request_payload)
    assert response.status_code == 200, f"Response_code received = {response.status_code} but expected 200!"

    print('Test case 4 passed!')
    print_response(response)


# Test Case 5: Test to see if we can delete the user
def test_delete_user():
    url = f"{base_url}/users/2"
    response = requests.delete(url)

    assert response.status_code == 204, f"Response_code received = {response.status_code} but expected 204!"

    print('Test case 5 passed!')
    print_response(response)


# Test Case 6: Test to see if can register successfully

def test_register_success():
    url = f"{base_url}/register"
    request_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, json=request_payload)

    assert response.status_code == 200, f"Response_code received = {response.status_code} but expected 200!"

    print('Test case 6 passed!')
    print_response(response)


# Test Case 7: Test to see we cannot register successfully, if password is missing
def test_register_not_success():
    url = f"{base_url}/register"
    request_payload = {
        "email": "sydney@fife",
    }
    response = requests.post(url, json=request_payload)

    assert response.status_code == 400, f"Response_code received = {response.status_code} but expected 200!"
    data = response.json()
    assert data['error'] == 'Missing password', "Error message is not correct"

    print('Test case 7 passed!')
    print_response(response)


# Test Case 8: Test to see if can login successfully

def test_login_success():
    url = f"{base_url}/login"
    request_payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url, json=request_payload)

    assert response.status_code == 200, f"Response_code received = {response.status_code} but expected 200!"

    print('Test case 8 passed!')
    print_response(response)


# Test Case 9: Test to see we cannot login successfully, if password is missing
def test_login_not_success():
    url = f"{base_url}/login"
    request_payload = {
        "email": "peter@klaven",
    }
    response = requests.post(url, json=request_payload)

    assert response.status_code == 400, f"Response_code received = {response.status_code} but expected 200!"
    data = response.json()
    assert data['error'] == 'Missing password', "Error message is not correct"

    print('Test case 9 passed!')
    print_response(response)


if __name__ == '__main__':
    test_get_users()
    # User present
    test_get_a_user(2)

    # If User is not present. Uncomment line 75 to test if user not present. Assertion/test fails as it throws 404
    # test_get_a_user(23)

    test_create_user()
    test_update_user()
    test_delete_user()
    test_register_success()
    test_register_not_success()
    test_login_success()
    test_login_not_success()
