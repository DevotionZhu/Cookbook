class Person:
    def __init__(self, name):
        self.first_name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self.name = value

    @name.deleter
    def name(self):
        raise AttributeError('can not delete attribute')

class SubPerson(Person):
    @property
    def name(self):
        print('getting name')
        return super().name

    # @name.setter






