import pytest
from modules import TestsAPI as testAPI

################### PET ###################
@pytest.mark.parametrize("json, expected_status_code", [
    ({
    "id": 18,
    "category": {
        "id": 15,
        "name": "string"
    },
    "name": "this is a dog",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 0,
        "name": "string"
        }
    ],
    "status": "available"
    }, 200),
    ({"type": "this is not a dict"}, 405)
])
def test_add_new_pet(json, expected_status_code):
    testAPI.add_new_pet(json, expected_status_code)
    

@pytest.mark.parametrize("status, expected_status_code", [
    ("available", 200),
    ("pending", 200),
    ("sold", 200),
    ("some status", 400),
])
def test_get_pets_by_status(status, expected_status_code):
    testAPI.get_pets_by_status(status, expected_status_code)
    
    

@pytest.mark.parametrize("id, expected_status_code", [
    (15, 200),
    ("sold", 400),
    (849416185418512837373737537, 404)
])
def test_get_pet_by_id(id, expected_status_code):
    testAPI.get_pet_by_id(id, expected_status_code)


    
@pytest.mark.parametrize("id, expected_status_code", [
    (18, 200),
    ("sold", 400),
    (849416185418512837373737537, 404)
])
def test_delete_pet(id, expected_status_code):
    testAPI.delete_pet(id, expected_status_code)


################### PET ###################
@pytest.mark.parametrize("username, expected_status_code", [
    ("test", 200),
    (4456, 400),
    ("Hello Mr test", 404)
])
def test_get_user_by_username(username, expected_status_code):
    """Retrieves user by username"""
    testAPI.get_user_by_username(username, expected_status_code)


@pytest.mark.parametrize("json, expected_status_code", [
    ({
    "id": 100,
    "username": "testtatata",
    "firstName": "Mr. User",
    "lastName": "Mr. his last name",
    "email": "test",
    "password": "thisisapassword",
    "phone": "string",
    "userStatus": 0
    }, 200),
    ({
    "id": 10,
    "username": "testtatataggzgezgzg",
    "firstName": "Mr. Userge gzeg zeg zeg zeg zeg ez",
    "lastName": "Mr. his last name",
    "email": "test",
    "password": "thisisapassword",
    "phone": "string",
    "userStatus": 0
    }, 200),
    ({}, 200),
    ("should default", 200)
])
def test_create_user(json, expected_status_code):
    testAPI.create_user(json, expected_status_code)


@pytest.mark.parametrize("username, password, expected_status_code", [
    ("testtatata", "thisisapassword", 200),
    ("testtatata", 15466, 400),
    ("", "thisisapassword", 400)
])
def test_login_user(username, password, expected_status_code):
    testAPI.login_user(username, password, expected_status_code)
    

@pytest.mark.parametrize("expected_status_code", [
    (200), (400)
])
def test_logout_user(expected_status_code):
    testAPI.logout_user(expected_status_code)
    
    

@pytest.mark.parametrize("username, json, expected_status_code", [
    ("testtatata", {
    "id": 100,
    "username": "testtatata",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
    }, 200)
])
def test_update_user(username, json, expected_status_code):
    testAPI.update_user(username, json, expected_status_code)
    

@pytest.mark.parametrize("username, expected_status_code", [
    ("testtatata", 200),
    (4456, 400),
    ("Hello Mr test", 404)
])
def test_delete_user(username, expected_status_code):
    """Retrieves user by username"""
    testAPI.delete_user_by_username(username, expected_status_code)