import random

import requests
import pytest

url = r"https://hbs-ob-stage.herokuapp.com"
mobile_no = r"+91{0}".format(random.randint(9000000000, 9999999999))
str_value = random.randint(10000, 100000)
otp = 111111


@pytest
def checkStatus():
    resp = requests.get("{0}/status".format(url))
    assert (resp.status_code == 200), str(resp.status_code)
    assert ((resp.json())['status'] is True), "Status code is not True"


@pytest
def createUser():
    json_body = {
        "name": "Test_Name_{0}".format(str(str_value)),
        "phone": mobile_no,
        "email": "Test_Name_{0}@hashedin.com".format(str(str_value)),
        "password": "admin",
        "otp": otp
    }
    resp = requests.post(url="{0}/user".format(url), json=json_body)
    assert (resp.status_code == 201), str(resp.status_code)
    assert (resp.text == '"User Created"\n')


@pytest
def getOtp():
    json_body = {
        "phone": mobile_no
    }
    resp = requests.post(url="{0}/get_register_otp".format(url), json=json_body)
    assert (resp.status_code == 200), str(resp.status_code)


@pytest
def deleteUser():
    json_body = {
        "phone": mobile_no,
        "otp": otp
    }
    resp = requests.delete(url="{0}/user".format(url), json=json_body)
    assert (resp.status_code == 200), str(resp.status_code)


@pytest
def editUser():
    str_new_value = random.randint(10000, 100000)
    json_body = {
        "name": "Test_Name_{0}".format(str(str_new_value)),
        "phone": mobile_no,
        "email": "Test_Name_{0}@hashedin.com".format(str(str_new_value)),
        "password": "admin",
        "otp": otp
    }
    resp = requests.put(url="{0}/user".format(url), json=json_body)
    assert (resp.status_code == 200), str(resp.status_code)


@pytest
def loginOtp():
    json_body = {
        "phone": mobile_no
    }
    resp = requests.post(url="{0}/get_otp".format(url), json=json_body)
    assert (resp.status_code == 200), str(resp.status_code)


@pytest
def authenticate_password():
    json_body = {
        "phone": mobile_no,
        "LoginType": "password",
        "password": "admin"
    }
    resp = requests.post(url="{0}/authenticate".format(url), json=json_body)
    assert (resp.status_code == 201), str(resp.status_code)
    global data
    data = resp.json()
    print(data['access_token'])


@pytest
def authenticate_otp():
    json_body = {
        "phone": mobile_no,
        "LoginType": "OTP",
        "otp": otp
    }
    resp = requests.post(url="{0}/authenticate".format(url), json=json_body)
    assert (resp.status_code == 201), str(resp.status_code)
    global data
    data = resp.json()


@pytest
def testlogin():
    headers = {"Authorization": "Bearer {0}".format(data['access_token'])}
    resp = requests.get(url="{0}/protected_test".format(url), headers=headers)
    assert (resp.status_code == 200), str(resp.status_code)





