"""
Rest API / JSON - String / Python - Dictionary
"""

# Example from JSON Place Holder / Users / 1

print('example from JSON place holder / users')
users = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'address': {
        'street': 'Kulas Light',
        'suite': 'Apt. 556',
        'city': 'Gwenborough',
        'zipcode': '92998-3874',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
        }
    }}
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address']['street'])
print(users['address']['suite'])
print(users['address']['city'])
print(users['address']['zipcode'])
print(users['address']['geo']['lat'])
print(users['address']['geo']['lng'])

# Mengolah Python Dictionary jadi JSON dan Sebaliknya

print('\nmengolah python dictionary jadi JSON dan sebaliknya')
print(users)
print(type(users))

# Python-Dict to JSON-String
print('\npython-dict to json-string')
import json
result = json.dumps(users)
print(result)
print(type(result))

# JSON-String to Python-Dict
print('\njson-stringt to python-dict')
with open('result.json', 'w') as file:
    json.dump(users,file)
