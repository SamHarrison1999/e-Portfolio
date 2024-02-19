class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    name = property(get_name, set_name)
    age = property(get_age, set_age)


c = Person("Calvin", 6)
print(c.name)
print(c.age)
c.name = "Hobbes"
c.age = 8
print(c.name)
print(c.age)