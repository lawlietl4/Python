# dictionary
person = {
    "first_name": "John",
    "last_name": "smith",
    "age": 21,
}

# dictionary
# key - unique
# value - any data type

person["first_name"] = "Gary"
person["credit_rating"] = 650

numbers = [1,2,3]

print(numbers[1]) #sets can access ordinal positions
print(person["first_name"]) #access items by key - not ordinal position

keys = set(person.keys())
print(keys)

complexDict = {
    "name": "jane",
    "credit_cards": [
        {
            "type": "VISA",
            "number": 4111111111111111,
        },
        {
            "type": "AMEX",
            "number": 84928842983563,
        },
    ]
}

#list comprehension

# print(count)
