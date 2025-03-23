BENCHMARK = 95

# DEFINING VARIABLES
firstscore = int(input("Enter the first score: \n"))
secondscore = int(input("Enter the second score: \n"))
thirdscore = int(input("Enter the third score: \n"))

# CALCULATING THE AVERAGE
average = (firstscore + secondscore + thirdscore) / 3

# DISPLAYING THE AVERAGE
print(f"The average score is: {average:.1f}")

# # CONGRATULATING THE STUDENT
if average >= BENCHMARK:
    print("Congratulations!\nThat is a great average!")
else:
    print("You no try boss!\nPlease give up!\nNo try again!")

# res="Congrats" if average >= BENCHMARK else "You no try boss!\nPlease give up!\nNo try again!"

# res = ("No", "Congrats") [average >= BENCHMARK]

# res = "A" if average >= 80 and average <= 89 else "B" if average >= 70 and average <= 79 else "C" if average >= 60 and average <= 69 else "D" if average >= 50 and average <= 59 else "F"
# print(res)