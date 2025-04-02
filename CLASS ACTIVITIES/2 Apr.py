list_a=[2,4,6,8,10]
new_list=[]

#Printing the squares of the numbers in list_a
for i in list_a:
    i**=2
    print(i)

#Printing the squares of the numbers in list_a and adding them to new_list
for i in list_a:
    new_list.append(i**2)
print(new_list)

#Getting the sum of the squares of the numbers in list_a
holder=0
for a in new_list:
    holder+=a
print(f"the sum of the squares is {holder}")

#Getting the sum of the squares of the numbers in list_a that are greater than 20
nholder=0
for a in new_list:
    if a>20:
        nholder+=a
print(f"the sum of the squares greater than 20 is {nholder}")

#Sum of all numbers in list_a
sum_list=0
for a in list_a:
    sum_list+=a
print(f"The sum of all numbers in list_a is {sum_list}")

#Ask buyer what they want to buy. If that item is in the list, remove it. The cose should stop if all the items have been bought. If the item is not in the list, tell user it has run out and they shpuld choose something else. 

items = ["milk", "bread", "eggs", "cheese", "apples", "tomatoes", "bananas"]
user_order = input("What do you want to buy? ").lower()
while True:
    if user_order in items:
        items.remove(user_order)
        print(f"You have bought {user_order}.It has now been removed.")
        print(f"Items left are: ", end="")
        # for i in items:
        #         print(i, end=", ")
        print(items)
        if len(items) == 0:
            print("All items have been bought.")
            break
    else:
        print(f"{user_order} is not available. Please choose something else.")
        print(f"Items that are available are: {items}")
    user_order = input("What do you want to buy? ").lower()