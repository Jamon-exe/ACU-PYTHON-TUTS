numbers=[[2,3],[4,5],[6,7],[8,9,7]]

#finding the last two elements of the list
print(numbers[-2:])
#finding the first three elements of the list
print(numbers[:3])
#finding the first and last elements of the list
print(numbers[:4:3])

#printing the last element of the lists within the numbers list
for i in numbers:
    print(i[-1])
#     for j in i:
#         if j == i[-1]:
#             print(j)

#finding the sum of each list with the numbers list
holder=0
for i in numbers:
    for j in i:
        holder+=j
    print (f"sum is {holder}")
    holder=0
#alternative method of finding the sum of each list with the numbers list
for i in numbers:
    jay=sum(i)
    print(jay)
