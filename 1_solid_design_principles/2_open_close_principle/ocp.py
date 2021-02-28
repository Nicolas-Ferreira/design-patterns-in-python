# OCP
# OPERN for EXTENSION
# CLOSE for MODIFICATION

# Suggest that when you add new functionality you add it by extension NOT by modification
# Once the class has been tested, you should not modified, instead you should extended

# You do not want to end up in a situaction where you keep modifying code thats already been written, testing
# and in production. It's much better to define a bunch of base classes and then when you need new criterias
# you define new specifications


from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    # This approach does not scale, because when you need a new filter you have to modify the class adding a new function
    # It is breaking the OCP
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_color_and_size(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p

# Solutions that do not break the OCP

# ############# #
# Specification #
# We will override these methods with filter criterias
class Specification:
    # Determines if an item satisfy a particular criteria
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

# Supose you want to filter by color
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

# Supose you want to filter by size
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

# To combine specfications and create multiple condition filters
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Using antipattern
    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'  - {p.name} is green')

    # Using OCP pattern
    bf = BetterFilter()

    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'  - {p.name} is green')

    print('Large products (new):')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f'  - {p.name} is large')

    print('Large Blue products (new)')
    large_blue = AndSpecification(
        large,
        ColorSpecification(Color.BLUE)
    )
    for p in bf.filter(products, large_blue):
        print(f'  - {p.name} is large and blue')
