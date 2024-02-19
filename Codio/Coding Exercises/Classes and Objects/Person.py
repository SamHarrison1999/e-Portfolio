import inspect


class Person:
    count = 0

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

    @classmethod
    def print_count(cls, ):
        return cls.count

    @classmethod
    def print_self(cls, ):
        for i in inspect.getmembers(Person):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    print(i)

    def print_self(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Weight: " + str(self.weight_in_lbs) + "lbs")
        print("Height: " + str(self.height_in_inches) + " inches")
        print("BMI: " + str(self.calc_bmi()))

    def bmi_range_checker(self):
        bmi = self.calc_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25.0:
            return "Healthy Weight"
        elif 25.0 <= bmi < 30.0:
            return "Overweight"
        elif bmi > 30.0:
            return "Obesity"


if __name__ == '__main__':
    p = Person('Tom', 'Thumb', 150, 62)

    people = [p]

    for person in people:
        print(person.first_name)

    print(p.calc_bmi())
    print(Person.print_count())
    p.print_self()
    Person.print_self(p)
    print(p.bmi_range_checker())
