#!/usr/bin/python3

def test_user_status():
    users = { 'Betsafe': 'Active', 'Betika': 'Inactive', 'Sportpesa': 'Active', 'Mamili':'Inactive'}

    del_users = {user: status for user, status in users.items() if status == 'Inactive'}
    active_users = {user: status for user, status in users.items() if status == 'Active'}

    # Optionally, if you still want to delete inactive users from the original dictionary
    for user in del_users:
        del users[user]

    assert del_users == {'Betika': 'Inactive', 'Mamili': 'Inactive'}, f"Expected {{'Betika': 'Inactive', 'Mamili': 'Inactive'}}, but got {del_users}"
    assert active_users == {'Betsafe': 'Active', 'Sportpesa': 'Active'}, f"Expected {{'Betsafe': 'Active', 'Sportpesa': 'Active'}}, but got {active_users}"
    assert users == {'Betsafe': 'Active', 'Sportpesa': 'Active'}, f"Expected {{'Betsafe': 'Active', 'Sportpesa': 'Active'}}, but got {users}"

if __name__ == "__main__":
    test_user_status()
    print("All tests passed!")