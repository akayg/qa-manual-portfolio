import requests

def test_valid_login():
    url="https://reqres.in/api/login"
    headers={
        "x-api-key":"reqres-free-v1",
        "Content-Type":"application/json"

    }

    data={
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"

    }

    response= requests.post( url ,json=data , headers=headers)
    assert response.status_code==200
    assert "token" in response.json()


def test_login_missing_password():
    url="https://reqres.in/api/login"
    headers={
        "x-api-key":"reqres-free-v1",
        "Content-Type":"application/json"

    }

    data={
        "email":"eve.holt@reqres.in"
    }

    response=requests.post(url,json=data,headers=headers)
    assert response.status_code==400,"Expected 400 Bad Requests"
    assert "error" in response.json(), "Expected error in response"
    assert response.json()["error"] == "Missing password"

