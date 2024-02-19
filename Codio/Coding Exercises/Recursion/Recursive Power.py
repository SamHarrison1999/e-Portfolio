def recursive_power(n1, n2):
    if n2 == 0:
        return 1
    else:
        return n1 * recursive_power(n1, n2 - 1)


print(recursive_power(5, 3))
print(recursive_power(4, 5))
