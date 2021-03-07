import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('John', Address('123 London Road', 'London', 'UK'))
print(john)

# Suppose we want to create a new person that lives with John
# You might be temped to make the followong:
jane = john
jane.name = 'Jane'
print(john)
print(jane)

# Output
# John lives at 123 London Road, London, UK
# Jane lives at 123 London Road, London, UK
# Jane lives at 123 London Road, London, UK
# jane = john refer to the same object

# Solution
john = Person('John', Address('123 London Road', 'London', 'UK'))
jane = copy.deepcopy(john) # use deep copy to copy and break link
jane.name = 'Jane'
jane.address.street_address = '124 London Road'
print(john)
print(jane)
