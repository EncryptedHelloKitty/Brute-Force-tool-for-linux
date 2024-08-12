import requests

def try_login(username, password):
    url = "http://localhost/login"  # Replace with your target URL
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)

    if "Login successful" in response.text:  # Adjust according to your target's response
        return True
    return False
