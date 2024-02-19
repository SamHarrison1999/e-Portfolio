class TestClass:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
        self._sum = 0

    def get_num1(self):
        return self._num1

    def set_num1(self, new_value):
        self._num1 = new_value

    def get_num2(self):
        return self._num2

    def set_num2(self, new_value):
        self._num2 = new_value

    def get_sum(self):
        return self._sum

    def set_sum(self, new_value):
        self._sum = new_value


obj = TestClass(5, 7)
print(obj.get_num1())
print(obj.get_num2())
obj.sum(obj.num1 + obj.num2)
print(obj.get_sum())