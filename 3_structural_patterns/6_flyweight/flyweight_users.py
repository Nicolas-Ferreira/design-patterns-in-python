import random
import string
import sys


# This class is not efficient
class User:
    def __init__(self, name):
        self.name = name


# Flyweight class
class User2:
    # strings list with names
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            # Get names indexes in names list or add it if not exist
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1
        self.names = [
            get_or_add(x) for x in full_name.split(' ')
        ]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for x in range(8)]
    )


if __name__ == '__main__':
    users = []

    # artificial names
    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    # create user names samples
    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))

    u2 = User2('Jim Jones')
    u3 = User2('Frank Jones')
    print(u2.names)
    print(u3.names)
    print(User2.strings)

    users2 = []

    for first in first_names:
        for last in last_names:
            users2.append(User2(f'{first} {last}'))
