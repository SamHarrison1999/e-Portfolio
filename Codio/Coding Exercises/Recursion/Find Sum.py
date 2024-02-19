def find_sum(n):
    """Recursively calculate the sum of the first n numbers"""
    if n == 0:
        return 0
    else:
        return(n + find_sum(n-1))
