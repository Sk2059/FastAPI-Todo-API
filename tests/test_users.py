from tests.conftest import client

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "my fastapi application is running"
    }

def test_register_user():
    response = client.post(
        "/users/register",
        json={
            "username": "sabin2",
            "email": "sabinam4@example.com",
            "password": "password1234"
        }
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 201

def test_login():
    client.post(
        "/users/register",
        json={
            "username": "login_user",
            "email": "login@test.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/users/login",
        data={
            "username": "login@test.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data