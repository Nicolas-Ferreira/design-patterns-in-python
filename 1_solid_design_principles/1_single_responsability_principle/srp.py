# SRP
# Also known as Separation of concern (SOC)

# If you have a class, that class should have its primary responsability
# and it should not take on other responsabilities

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # the following methods are breaking the SRP
    # because we are adding secondary responsabilities (persistance)
    # we should take this methods and create a new class so we can reuse the persistance methods
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistanceManager():
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

# Use the persistance manager class to save content to file
file = 'journal.txt'
PersistanceManager.save_to_file(j, file)
