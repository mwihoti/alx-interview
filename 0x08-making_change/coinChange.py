#!/usr/bin/python3

users = { 'Betsafe': 'Active', 'Betika': 'Inactive', 'Sportpesa': 'Active', 'Mamili':'Inactive'}
active_users = {}
del_users = {}

for user, status in users.copy().items():
    if status == 'Inactive':
        del_users[user]  = status
        del users[user]
    elif status == 'Active':
        active_users[user] = status

print(del_users)
print(active_users)