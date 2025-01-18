#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================== #
####    Information     ####
# ------------------------ #
# Version   : V0
# Author    : Kamal Atmeh
# Date      : 18/01/2025

####    Objective        ####
# ------------------------ #
# This script is used to define API functions for testing PetStore

####    To Do         ####
# ------------------------ #

####    Packages        ####
# ------------------------ #
from setup import setup_modules as stp
import pytest
import requests

####    Variables        ####
# ------------------------ #
BASE_URL = "https://petstore.swagger.io/v2"
ENDPOINTS = {
    "pet": f"{BASE_URL}/pet",
    "store": f"{BASE_URL}/store",
    "user": f"{BASE_URL}/user"
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'test_key_corti'  # If authentication is needed
}

####   Functions        ####
# ------------------------ #
@pytest.fixture(scope="session")
def base_url():
    """Returns the base URl of the API"""
    return BASE_URL

################### General function ###################
def request_endpoint(method: str, endpoint: str, key: str = None, params = None,
                     headers = None, data = None, files = None, json = None) -> requests.models.Response:
    """General method that can be applied to send requests to the PetStore APIs

    Args:
        method (str): Defines the type of the request. Get, Post, Delete, Update.
        endpoint (str): The endpoint to which the request is sent
        key (str, optional): An optional key for the endpoint
        params (_type_, optional): Optional parameters to be sent to the endpoint

    Returns:
        requests.models.Response: Returns the request's reponse
    """
    url = f"{ENDPOINTS[endpoint]}/{key}" if key else ENDPOINTS[endpoint]
    return getattr(requests, method)(url, params = params, headers = headers,
                                     data = data, files = files, json = json)


def get_pet_endpoint(key: str = None, params = None):
    return request_endpoint("get", "pet", key, params)


def post_pet_endpoint(key: str = None, params = None, headers = None, json = None):
    return request_endpoint("post", "pet", key, params = params, headers = headers, json = json)


def delete_pet_endpoint(key: str = None, params = None):
    return request_endpoint("delete", "pet", key, params)


def get_store_endpoint(key: str = None, params = None):
    return request_endpoint("get", "store", key, params)


def post_store_endpoint(key: str = None, params = None, headers = None, json = None):
    return request_endpoint("post", "store", key, params = params, headers = headers, json = json)


def delete_store_endpoint(key: str = None, params = None):
    return request_endpoint("delete", "store", key, params)


def get_user_endpoint(key: str = None, params = None):
    return request_endpoint("get", "user", key, params)


def post_user_endpoint(key: str = None, params = None, headers = None, json = None):
    return request_endpoint("post", "user", key, params = params, headers = headers, json = json)


def delete_user_endpoint(key: str = None, params = None):
    return request_endpoint("delete", "user", key, params)


def put_user_endpoint(key: str = None, params = None, headers = None, json = None):
    return request_endpoint("put", "user", key, params = params, headers = headers, json = json)


################### PET ###################
def add_new_pet(json: dict = None, expected_status_code = 200):
    """Adds a new pet to the store by providing a json body to the endpoint

    Args:
        json (dict, optional): A JSON body that contains the id, name, and status of the pet.
        Defaults to None.
    """
    response = post_pet_endpoint(headers = headers, json = json)
    
    # Assert status code
    assert response.status_code == expected_status_code, f"Expected {expected_status_code} but got {response.status_code}"
    
    # Verify that pet has been added by running get pet by id endpoint
    get_pet_by_id(json.get("id"))


def get_pets_by_status(status: str, expected_status_code = 200):
    """Retrieves all pets with a particular status.

    Args:
        status (str): The status of the pets to be retrieved. 
    """    
    response = get_pet_endpoint('findByStatus', {"status": status})
    
    # Assert status code
    assert response.status_code == expected_status_code, f"Expected {expected_status_code} but got {response.status_code}"

    # Assert response is JSON
    assert response.headers["Content-Type"] == "application/json", "Response is not JSON"

    # Parse and validate response body
    pets = response.json()
    assert isinstance(pets, list), "Response is not a list"
    for pet in pets:
        assert pet["status"] == status, f"Unexpected status: {pet['status']}"


def get_pet_by_id(id: int, expected_status_code = 200):
    """Retrieves a pet by providing its ID

    Args:
        id (int):The ID of the pet to be retrieved
        expected_status_code (int, optional): The expected status of the request.
        To be set in case the response is expected to be anything other than 200. Defaults to 200.
    """
    response = get_pet_endpoint(id)
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected status code {expected_status_code} but got {response.status_code}'
    
    # Verify ID of pet
    if expected_status_code == 200:
        assert response.json().get("id") == id, f'The pet ID should be {id}'
    

def delete_pet(id: int, expected_status_code = 200):
    """Deletes a pet from the store and verifies its deletion by running the get pet by ID endpoint.

    Args:
        id (int): The id of the pet to be deleted
    """
    response = delete_pet_endpoint(id)
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'
    if expected_status_code == 200:
        assert response.json().get('message') == str(id), f'Message should be {id}'
    
    # Verify that pet does not exist
    get_pet_by_id(id, 404)


################### USER ###################
def get_user_by_username(username: str, expected_status_code = 200):
    
    response = get_user_endpoint(username)
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'
    
    # Verify username of user
    if expected_status_code == 200:
        assert response.json().get("username") == username, f'The username should be {username}'


def update_user(username: str, json = None, expected_status_code = 200):
    
    # Retrieve initial information
    initial_json = get_user_by_username(username)
    
    response = put_user_endpoint(username, headers = headers, json = json)
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'
    
    # Assert that user has been updated
    assert initial_json != response.json(), f'Expected {json} but got {response.json()}'
    
    
def delete_user_by_username(username: str, expected_status_code = 200):
    
    response = delete_user_endpoint(username)
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'
    
    # Verify that user has been deleted
    get_user_by_username(username, 404)


def create_user(json: dict = None, expected_status_code = 200):
    response = post_user_endpoint(headers = headers, json = json)
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'
    
    # Verify that user has been created
    get_user_by_username(json.get('username'))


def login_user(username: str, password: str, expected_status_code = 200):
    response = get_user_endpoint('login', params = {'username': username, 'password': password})
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'


def logout_user(expected_status_code = 200):
    response = get_user_endpoint('logout')
    
    # Assert status code
    assert response.status_code == expected_status_code, f'Expected {expected_status_code} but got {response.status_code}'