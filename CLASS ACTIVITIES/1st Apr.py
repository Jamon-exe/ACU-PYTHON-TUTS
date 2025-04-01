a = ['apple', 'banana', 'cherry'] # A list of fruits
b = [1, 2, 3, 4, 5] # A list of numbers
c = [True, False, True] # A list of boolean values
d = ['apple', 1, True] # A list with mixed data types

#A list is a collection of items in a particular order. It stores multiple items in a single variable.
#A list is created by placing all the items (elements) inside square brackets [], separated by commas.
# [] is used to create a list.
# () is used to create a tuple.
# {} is used to create a set.

#---------------------------------------
#Lists are mutable, meaning they can be changed. You can add, remove, or change items in a list after it has been created.
#For example, you can add a new item to the list using the append() method:
a.append("orange")
print(a) # Output: ['apple', 'banana', 'cherry', 'orange']
#You can also remove an item from the list using the remove() method:
a.remove("banana")
print(a) # Output: ['apple', 'cherry', 'orange']

#--------------------------------------
#You can change an item in the list by accessing it using its index (position in the list):
a[0] = "kiwi"
print(a) # Output: ['kiwi', 'cherry', 'orange']
#You can also access items in a list using negative indexing, which starts from the end of the list:
print(a[-1]) # Output: 'orange' (last item in the list)
#You can also use slicing to access a range of items in the list:
print(a[1:3]) # Output: ['cherry', 'orange'] (items from index 1 to 2)


#-------------------------------
#Lists can be iterated over using a for loop:
for fruit in a:
    print(fruit) # Output: 'kiwi', 'cherry', 'orange' (each item in the list)
#You can also use the range() function to iterate over a list by index:
for i in range(len(a)):
    print(a[i]) # Output: 'kiwi', 'cherry', 'orange' (each item in the list by index)
print("\n\n")

#---------------------------------------
#You can also use the in keyword to check if an item is in a list:
print("kiwi" in a) # Output: True (kiwi is in the list)
#You can also use the not in keyword to check if an item is not in a list:
print("banana" not in a) # Output: True (banana is not in the list)
print("\n\n")

#----------------------------------------
#You can also use the index() method to find the index of an item in a list:
print(a.index("cherry")) # Output: 1 (index of cherry in the list)
#You can also use the count() method to count the number of occurrences of an item in a list:
print(a.count("kiwi")) # Output: 1 (number of occurrences of kiwi in the list)
#You can also use the sort() method to sort a list in ascending order:
a.sort()
print(a) # Output: ['cherry', 'kiwi', 'orange'] (sorted list)
#You can also use the reverse() method to reverse the order of a list:
a.reverse()
print(a) # Output: ['orange', 'kiwi', 'cherry'] (reversed list)
#You can also use the copy() method to create a shallow copy of a list:
a_copy = a.copy()
print(a_copy) # Output: ['orange', 'kiwi', 'cherry'] (copy of the list)
#You can also use the clear() method to remove all items from a list:
a.clear()
print(a) # Output: [] (empty list)
#You can also use the extend() method to add multiple items to a list:
a.extend(["grape", "pear"])
print(a) # Output: ['grape', 'pear'] (list with multiple items added)
#You can also use the insert() method to add an item at a specific index in a list:
a.insert(1, "banana")
print(a) # Output: ['grape', 'banana', 'pear'] (item inserted at index 1)
#You can also use the pop() method to remove an item at a specific index in a list:
a.pop(1)
print(a) # Output: ['grape', 'pear'] (item removed at index 1)
#You can also use the del keyword to remove an item at a specific index in a list:
del a[0]
print(a) # Output: ['pear'] (item removed at index 0)
#You can also use the slice assignment to change a range of items in a list:
a[0:1] = ["apple", "banana"]
print(a) # Output: ['apple', 'banana'] (range of items changed)
#You can also use the list() constructor to create a list from a string:
print("\n\n")

#---------------------------------------
a = list("hello")
print(a) # Output: ['h', 'e', 'l', 'l', 'o'] (list created from string)
#You can also use the list() constructor to create a list from a tuple:
a = list((1, 2, 3))
print(a) # Output: [1, 2, 3] (list created from tuple)
#You can also use the list() constructor to create a list from a set:
a = list({1, 2, 3})
print(a) # Output: [1, 2, 3] (list created from set)
#You can also use the list() constructor to create a list from a dictionary:
a = list({"a": 1, "b": 2, "c": 3})
print(a) # Output: ['a', 'b', 'c'] (list created from dictionary keys)
#You can also use the list() constructor to create a list from a range:
a = list(range(5))
print(a) # Output: [0, 1, 2, 3, 4] (list created from range)
#You can also use the list() constructor to create a list from a generator expression:
a = list(x**2 for x in range(5))
print(a) # Output: [0, 1, 4, 9, 16] (list created from generator expression)
print("\n\n")

#---------------------------------------
#You can also use the len() function to get the number of items in a list:
print(len(a)) # Output: 3 (number of items in the list)
print("\n\n")

#--------------------------------------
ama= 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(type(ama)) # Output: <class 'tuple'>
# ama[0] = 2 # This will raise a TypeError because tuples are immutable
# ama.append(11) # This will also raise a TypeError because tuples do not have an append() method

#Lists can be nested, meaning you can have lists within lists. For example:

#Lists can contain items of different data types, including strings, integers, and other lists.
#Lists are ordered, meaning the items have a defined order, and that order will not change.
print("\n\n")

#----------------------------------------
veg_fruits = ['apple', 'mango', 'pineapple']
add = ['tomato', 'cucumber', 'onion']
veg_fruits.extend(add)
for each in veg_fruits:
    print(each)
    if each == 'tomato':
        break
print("\n\n")

#----------------------------------------
for each in veg_fruits:
    if each == 'pineapple':
        continue
    print(each)
print("\n\n")

#----------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
for x in numbers:
    print(x**2)
print ("Congratulations!")
print("\n\n")
#---------------------------------------

print([x**2 for x in numbers if x % 2 == 0])
print("\n\n")

#---------------TASK----------------------------

#---------------------------------------
for x in numbers:
    print(x**2)
print("\n")
#---------------------------------------
for x in numbers:
    if x == 3 or x == 5 or x == 4:
        continue
    print(x**2)
print("\n")
#---------------------------------------
for x in numbers:
    x**=2
    if x >=10 and x <=40:
        print(x)
print("\n")

#---------------------------------------
n=0
for x in numbers:
    x**=2
    n+=x
print(n)