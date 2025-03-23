# i = 0
# while i < 4:
#     i = i + 1


# ----------------------------------------
dail= "0"
attempts = 3

while dail != "*170#":
    dail= input("Input the Dail: ")  
    if dail == "*170#":
        print ("You have successfully loaded your airtime")
        
        break
    else:
        print ("Invalid code") 
    attempts -= 1
    print (f"You have {attempts} more attempts left.")
    if attempts <= 0:
        break