import requests

BASE_URL = "http://127.0.0.1:5000"


# Test name functions
def test_hello_world():
    response = requests.get(f"{BASE_URL}/")
    print(f"Main page: status {response.status_code} - {response.text}")


def test_save_name(data):
    response = requests.post(f"{BASE_URL}/name", json=data)
    print(f"Save name: status {response.status_code} - {response.text}")


def test_get_name():
    response = requests.get(f"{BASE_URL}/name")
    print(f"Get name: status {response.status_code} - {response.text}")


#############################################################################################

# Test user functions
def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    print(f"Get all users: status {response.status_code} - {response.json()}")


def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"Get user {user_id}: status {response.status_code} - {response.json()}")


def test_create_user(data):
    response = requests.post(f"{BASE_URL}/users", json=data)
    print(f"Create user: status {response.status_code} - {response.json()}")


def test_update_user(user_id, data):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data)
    print(f"Update user {user_id}: status {response.status_code} - {response.json()}")


def test_delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    print(f"Delete user {user_id}: status {response.status_code} - {response.json()}")


# Run all tests
if __name__ == "__main__":
    test_hello_world()

    print("Testing Name Endpoints:")
    test_save_name({"name": "Dave"})
    test_get_name()

    print("\nTesting User Endpoints:")
    test_get_all_users()
    test_get_user(101)
    test_create_user({"name": "Chris", "phone": "9876543"})
    test_get_all_users()
    test_update_user(101, {"name": "David", "phone": "5551234"})
    test_get_all_users()
    test_delete_user(101)
    test_get_all_users()
    test_get_user(103)
