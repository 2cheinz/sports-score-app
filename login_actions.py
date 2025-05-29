# login actions to use for utilizing the microservice my teammate has built
import requests
import json

LOGIN_URL = "http://localhost:3002"

# functions created based off of instructions from Owen Sexton's Microservice in Github https://github.com/Sextono/361_MicroserviceA

def create_account(username, password):
    url = f"{LOGIN_URL}/create"
    body = {"username": username, "password": password}
    response = requests.post(url, data=json.dumps(body), headers={"Content-Type": "application/json"})
    return response.status_code == 201

def login(username, password):
    url = f"{LOGIN_URL}/login"
    body = {"username": username, "password": password}
    response = requests.post(url, data=json.dumps(body), headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        return response.json()
    return None

def validate(token):
    url = f"{LOGIN_URL}/validate"
    body = {"token": token}
    response = requests.post(url, data=json.dumps(body), headers={"Content-Type": "application/json"})
    return response.status_code == 200

def logout(token):
    url = f"{LOGIN_URL}/logout"
    body = {"token": token}
    response = requests.post(url, data=json.dumps(body), headers={"Content-Type": "application/json"})
    return response.status_code == 200
