import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response_data)
print(login_response.status_code)

headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}


me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
print(me_response.json())
print(me_response.status_code)