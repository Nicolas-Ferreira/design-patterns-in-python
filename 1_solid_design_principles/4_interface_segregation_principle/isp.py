# ISP
# Not stick too many elements, methods into an interface

class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

# When you extends from the main interface maybe there are some functionalities that
# we do not need, for instance with old printers
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        # old printers do not send fax
        raise NotImplementedError('Old Fashioned Printers cannot send fax')

    def scan(self, document):
        # old printers do not scan
        raise NotImplementedError('Old Fashioned Printers cannot scan')


# Segregation means split the interface into separate parts so people can claim
# Instead of having the Machine Class you would have one class per functionality
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass

# Now you can combine the parts you need
class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.printer.scan(document)
