list_a = [1, 2, 3, 4, 5, 6, 7, 8]
list_b = [3, 4, 7, 10, 11]
for a in list_b:
    if a in list_a and a not in list_b:
        print(a)