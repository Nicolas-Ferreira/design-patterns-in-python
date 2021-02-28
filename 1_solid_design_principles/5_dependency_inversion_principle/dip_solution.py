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

# Solution: interface for relationships
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Relationships(RelationshipBrowser):  # Low level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    # Solution: move the searh method to the low level module
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

# High level modules
class Research:  # High level module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
