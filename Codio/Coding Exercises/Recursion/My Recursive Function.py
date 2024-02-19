def my_recursive_function(num):
    """Creates a recursive function"""
    if num < 0:
        return 1
    else:
        return num + my_recursive_function(num - 1)
    