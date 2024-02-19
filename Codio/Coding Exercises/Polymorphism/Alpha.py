class Alpha:
    def show(self):
        print("I am from class Alpha")

    def hello(self):
        print("Hello from Alpha")


class Bravo(Alpha):
    def show(self):
        print("I am from class Bravo")

    def hello(self):
        print("Hello from Bravo")





if __name__ == "__main__":
    # test_object = Alpha()
    test_object = Bravo()
    test_object.show()
    test_object.hello()
