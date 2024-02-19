class Median:
    def calculate_median(self, n1, n2, n3=None, n4=None, n5=None):
        if n3 is not None and n4 is not None and n5 is not None:
            numbers = [n1, n2, n3, n4, n5]
        elif n3 is not None and n4 is not None:
            numbers = [n1, n2, n3, n4]
        elif n3 is not None:
            numbers = [n1, n2, n3]
        else:
            numbers = [n1, n2]

        numbers.sort()
        median_index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            median = (numbers[median_index] + numbers[median_index - 1]) / 2
        else:
            median = numbers[median_index]
        return median


if __name__ == '__main__':
    m = Median()
    print(m.calculate_median(3, 5, 1, 4, 2))
    print(m.calculate_median(8, 6, 4, 2))
    print(m.calculate_median(9, 3, 7))
    print(m.calculate_median(5, 2))
