#-------------------
a=["carrot", 'cucumber', 'onion', 'apple', 2]
print(a[1], " ", a[-4])
a[2] = "cabbage"
print(a)
print("\t\t")

#-------------------
#SLICING
#Slicing is used to access a part of the list
print(a[2:4])
# To get everything from the list using slicing
print(a[:])
print("\t\t")


#-------------------
print(a[1:3])
print(a[-1:])
print(a[:-1])
print(a[-1])
print(a[0:-2])
print(a[4:])
print(a[-1:-4])

#-------------------
#EXPANDING THE ITEMS IN THE LIST
items =[1,2] * 3
#This will print the items in the list 3 times
print(items)

#-------------------
#ADDING ITEMS TO A LIST
a = [1,2,3]
b = ['a', 'b']
print(a+b)

#-------------------
#REMOVING ITEMS FROM A LIST
a = [1,2,3,4,5]
del a[1]
print(a)

#-------------------
#APPENDING ITEMS TO A LIST
a = [1,2,3,4,5]
a.append("apple")
print(a)

#--------------------------------------------
# min() returns the smallest number in the list
# max() returns the largest number in the list
# sum() returns the sum of all the numbers in the list
# min() and max() and sum() on a float or integer lists functions
a = [1,2,3,4,5]
print(min(a))
print(max(a))
print(sum(a))

#--------------------------------------------
#count() function
#count() returns the number of times an item appears in the list
a=[1,2,3,5,5,5,6,7,8,9,10]
print(a.count(5))

#--------------------------------------------
# extend() function
# extend() function is used to add items to a list
# extend() function is similar to the append() function
# append() function adds a single item to the list
# extend() function adds multiple items to the list
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print(a)