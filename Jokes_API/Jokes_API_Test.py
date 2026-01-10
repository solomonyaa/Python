import requests

BASE_URL = "http://127.0.0.1:5000"
categories = ("Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas")


def test_login(data):
    response = requests.post(f"{BASE_URL}/login", json=data)
    print(f"Login - status: {response.status_code} - {response.text}")


def test_return_joke():
    response = requests.get(f"{BASE_URL}/joke")
    print(f"Get Any Joke - status {response.status_code}: \n{response.text}")


def return_joke_by_category(category):
    response = requests.get(f"{BASE_URL}/joke/{category}")
    print(f"Get {category} Joke - status {response.status_code}: \n{response.text}")


if __name__ == '__main__':
    test_login({"user": "Dave", "password": "123456"})
    test_return_joke()
    print()
    for i in range(len(categories)):
        return_joke_by_category(categories[i])
        print()
