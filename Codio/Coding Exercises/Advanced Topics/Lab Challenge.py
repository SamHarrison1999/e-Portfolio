from Stats import Stats

if __name__ == '__main__':
    my_stats = Stats()

    print(my_stats.mean([8, 7, 3, 3, 1, 4, 9]))
    print(my_stats.median([8, 7, 3, 3, 1, 4, 9]))
    print(my_stats.mode([8, 7, 3, 3, 1, 4, 9]))