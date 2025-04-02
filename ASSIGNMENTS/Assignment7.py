#Assignmet 1
# Find out why a[-1:-4] returns an empty list

#Assignmet 2
# find other functions that can be used on a list. 

#-------------------SOLUTION----------------------
#Assignment 1
# Find out why a[-1:-4] returns an empty list
# Explanation: a[-1:-4] returns empty because the slice is going in wrong direction
# Slicing works left to right, but -1:-4 tries to go right to left
# To fix it, use a[-4:-1] or a[-1:-4:-1] with negative step

#Assignment 2
# List functions categorized:

# Functions that return new list:
# 1. sorted() - returns sorted list
# 2. list.copy() - returns copy of list
# 3. list + list - concatenation returns new list
# 4. list[::] - slicing returns new list

# Functions that modify list in-place:
# 1. list.sort() - sorts list
# 2. list.append() - adds element
# 3. list.extend() - adds elements from iterable
# 4. list.insert() - inserts element at index
# 5. list.remove() - removes element
# 6. list.pop() - removes and returns element
# 7. list.clear() - removes all elements
# 8. list.reverse() - reverses list

# Example:
nums = [3,1,4,1,5]
new_list = sorted(nums)  # Returns new list
nums.sort()             # Modifies original list
