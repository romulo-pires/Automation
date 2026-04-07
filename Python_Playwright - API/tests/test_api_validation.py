from playwright.sync_api import sync_playwright

def test_get_user(api_request):
        response = api_request.get("/api/users/1")

        print(response.status)

        print(response.json())

        assert response.status == 200

        data = response.json()
        assert data["data"]["id"] == 1
        assert data["data"]["email"] == "george.bluth@reqres.in"

    
def test_create_user(api_request):
        payload = {
            "email": "jd1@example.com",
            "password": "1234567890"
        }

        response = api_request.post("/api/users", data=payload)

        print(response.status)

        print(response.json())

        assert response.status == 201

        data = response.json()
        assert data["email"] == "jd1@example.com"
        assert data["password"] == "1234567890"


def test_login_user(api_request):
        payload = {
            "email": "rachel.howell@reqres.in",
            "password": "1234567890"
        }

        response = api_request.post("/api/login", data=payload)

        print(response.status)

        print(response.json())

        assert response.status == 200

        data = response.json()
        assert data["token"] == "QpwL5tke4Pnpja7X12"


def test_login_invalid_user(api_request):
        payload = {
            "email": "invalid@example.com",
            "password": "1234567890"
        }

        response = api_request.post("/api/login", data=payload)

        print(response.status)

        print(response.json())

        assert response.status == 400

def test_delete_user(api_request):
        response = api_request.delete("/api/users/1")

        print(response.status)

        assert response.status == 204

def test_update_user(api_request):
        payload = {
            "name": "Robert Smith",
            "job": "QA"
        }

        response = api_request.put("/api/users/1", data=payload)

        print(response.status)

        print(response.json())

        assert response.status == 200

        data = response.json()
        assert data["name"] == "Robert Smith"
        assert data["job"] == "QA"
        

def test_list_users(api_request):
        response = api_request.get("/api/users?page=2")

        print(response.status)

        print(response.json())

        assert response.status == 200

        data = response.json()
        assert len(data["data"]) > 0