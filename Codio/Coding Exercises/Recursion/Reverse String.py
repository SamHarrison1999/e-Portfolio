def reverse_string(s):
    if (len(s)) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]


print(reverse_string("cat"))
print(reverse_string("house"))
