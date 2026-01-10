"""
Test Suite for FocusFlow Scheduler API
Tests all endpoints with realistic scenarios including conflict detection.
Run this file while the Flask app (Scheduler_API.py) is running.
"""

import requests

BASE_URL = "http://127.0.0.1:5000"
separator = 150


def test_schedule_meeting(data):
    response = requests.post(f"{BASE_URL}/schedule", json=data)
    code = response.status_code
    res = response.json()

    if code == 201:
        res = rearrange_meeting_dict(response.json())
        print("New meeting scheduled:")
        print(f"Response code: {code}")
        print_dict(res)
    else:
        print(f"Response code: {code}, Response:{res}")

    print("=" * separator)


def test_next_meeting():
    response = requests.get(f"{BASE_URL}/next")
    code = response.status_code
    res = response.json()

    if code == 200:
        res = rearrange_meeting_dict(response.json())
        print("Next meeting:")
        print(f"Response code: {code}")
        print_dict(res)
    else:
        print(f"Response code: {code}, Response:{res}")

    print("=" * separator)


def test_remove_meeting():
    response = requests.post(f"{BASE_URL}/complete")
    code = response.status_code
    res = response.json()

    if code == 200:
        res = rearrange_meeting_dict(response.json())
        print("Removed meeting:")
        print(f"Response code: {code}")
        print_dict(res)
    else:
        print(f"Response code: {code}, Response:{res}")

    print("=" * separator)


def test_get_all_meetings():
    response = requests.get(f"{BASE_URL}/all")
    code = response.status_code
    res = response.json()

    if code == 200:
        res = rearrange_meeting_list(response.json())
        print("All meetings:")
        print(f"Response code: {code}")
        print_all_meetings(res)
    else:
        print(f"Response code: {code}, Response:{res}")

    print("=" * separator)


def rearrange_meeting_dict(api_dict):
    rearranged_dict = {
        'title': api_dict['title'],
        'start': api_dict['start'],
        'end': api_dict['end']
    }
    return rearranged_dict


def rearrange_meeting_list(api_list):
    rearranged_list = []
    for dictionary in api_list:
        rm = rearrange_meeting_dict(dictionary)
        rearranged_list.append(rm)
    return rearranged_list


def print_dict(api_dict):
    for key, value in api_dict.items():
        print(f"{key}: {value}, ", end="")
    print()


def print_all_meetings(meeting_list):
    for dictionary in meeting_list:
        print_dict(dictionary)


if __name__ == "__main__":
    test_schedule_meeting({"title": "NEW M", "start": "12:00", "duration": 60})
    test_schedule_meeting({"title": "NEW M 2", "start": "14:00", "duration": 60})
    test_next_meeting()
    test_get_all_meetings()
    test_remove_meeting()
    test_get_all_meetings()
    test_remove_meeting()
    test_remove_meeting()
    test_get_all_meetings()
    test_next_meeting()
