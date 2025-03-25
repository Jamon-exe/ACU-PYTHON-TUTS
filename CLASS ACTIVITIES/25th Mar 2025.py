print("Title: 25th Mar 2025")
print(list(range(4)))

print (list(range(1, 10, 2)))

print (list(range(3, 9)))

print (list(range(1, 10)))

print (list(range(10, 1, -1)), "\n\n")

#------------------------------------------
counter = 0
sumlist = 0

for a in [2, 3]:
    sumlist += a
    print(a)
    counter += 1

print("The amount of values in the list is ", counter, end=". ")
print (f"The sum of the list is {sumlist}.\n\n")

#------------------------------------------

amounts = [2,3,5,7,11,13,17,19,22,29,31,37,41,43,47,53,59,61,67,71,73,79,300,
           83,89,97,102,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
           178,181,191,193,197,199,230,223,227,229,233,239,241,251,257,263,269,271,
           277,288,283,293,300,307,311,313,317,331,337,347,349,353,359,367,373,379,383,
           389,397,401,409,419,424,431,433,439,443,449,457,461,463,467,479,487,491,
           499,503,509,521,523,546,547,557,563,569,571,577,587,593,599,601,607,613,
           617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,
           739,740,752,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,
           863,877,881,883,887,907,911,500,919,929,937,941,947,953,967,971,977,983,991,997,
           1000]
add=0
numofeven=0
numof300=0
totallist=0

for a in amounts:
    totallist += 1
    if a % 2 == 0:
        numofeven += 1
        add += a
    elif a > 300:
        numof300 += 1

#same range so the number will always be the same when it goes through the loop
for b in amounts:
    into=b
    for c in [300, 301]:
        pinto=c
        if into == pinto:
            break
    if into == pinto:
        break
print(pinto)
#------------------------------------------------
# print(f"The number that appears twice is {c}.")

print(f"The sum of the even numbers is {add}.")
print(f"The amount of even numbers is {numofeven}.")
print(f"The amount of numbers greater than 300 is {numof300}.")
print(f"The total amount of numbers in the list is {totallist}.")
#------------------------------------------
