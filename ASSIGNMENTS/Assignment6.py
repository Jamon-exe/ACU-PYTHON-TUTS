# pg 214 question 4, 5
#---------------------------------------------------------------
#Question 4
# Write a program that asks the user to enter the speed of a vehicle (in miles per hour) and how many hours it has traveled. It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. Here is an example of the output:
speed = int(input("What is the speed of the vehicle in mph: "))
time = int(input("How many hours has it traveled: "))
print("Hour\tDistance Traveled")
print("------------------------")
for i in range(1, time + 1):
    distance = speed * i
    print(i, "\t", end="")
    print(distance)

#---------------------------------------------------------------
#Question 6
tablenum = int(input("Enter the number of rows you want to display: "))
print ("Celsius\tFahrenheit")
print ("------------------------")
for i in range(1, tablenum + 1):
    Fahrenheit = 9/5 * i + 32
    print(i, "\t", Fahrenheit)


#Question 5
numyears = int(input("Enter the number of years: "))
