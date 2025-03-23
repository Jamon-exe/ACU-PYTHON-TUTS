def new_func (holder,i):
    holder = 0
    i = 1
    while i > 0:
        i = int(input("Number"))
        if (i % 2 == 0) and (i % 4 != 0):
            holder += i
    print (holder)

new_func(9,1)