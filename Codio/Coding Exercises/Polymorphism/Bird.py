class Bird:
    def fly(self):
        return "I am flapping my wings"


class Car:
    def drive(self):
        return "My wheels are turning"


def print_fly(obj):
    try:
        print(obj.fly())
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    my_bird = Bird()
    my_car = Car()
    print_fly(my_bird)
    print_fly(my_car)
