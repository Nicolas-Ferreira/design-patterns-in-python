# DIP
# High level modules or classes should not depend on low level modules instead they should depend on abstractions
# abstractions: abstract classes, interfaces
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

# High level modules
# attempting to find all of the children of Jonh for example
# the problem is that with the following class Reasearch we are accessing
# internal store mechanism of Relationships (a low level module)
# you cannot change the relations list to a DB in the future
# we could create an interface for the low level module
class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f'John has a child called {r[2].name}')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
