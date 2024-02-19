if __name__ == '__main__':
    my_string = "polymorphism"
    num1 = 3
    num2 = 5
    print(num1 * num2)
    print(int.__mul__(num1, num2))
    print(int.__add__(num1, num2))
    print(int.__sub__(num1, num2))
    print(int.__truediv__(num1, num2))
    print(int.__ne__(num1, num2))
    print(my_string * num1)