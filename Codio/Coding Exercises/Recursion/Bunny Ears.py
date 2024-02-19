def bunny_ears(bunnies):
    if bunnies < 1:
        return 0
    else:
        return 2 + bunny_ears(bunnies - 1)


print(bunny_ears(8))
print(bunny_ears(0))
