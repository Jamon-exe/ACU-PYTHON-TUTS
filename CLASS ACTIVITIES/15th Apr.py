def message():
    print("hello")

def messenger(name):
    return f"{name} ,Jamon King sane"

message()
Jamon= str( messenger("Jamon"))
print (Jamon)

firstname=""
lastname=""
rollnumber=""
unique_code=""

def firstname():
    global firstname
    firstname = input("Enter your first name: ")

def lastname():
    global lastname
    lastname = input("Enter your last name: ")

def rollnumber():
    global rollnumber
    rollnumber = input("Enter your roll number: ")

def inputvariables():
    firstname()
    lastname()
    rollnumber()

def verification_process():
    while True:
        inputvariables()

        if (len(firstname) <= 10 and len(lastname) <= 10 and len(rollnumber) <= 10) and (rollnumber.isdigit() and firstname.isalpha() and lastname.isalpha()):
            
            break
        else: 
            if  len(firstname) > 10:
                print("First name cannot contain more than 10 characters")
            if  len(lastname) > 10:
                print("Last name cannot contain more than 10 characters")
            if   len(rollnumber) > 10:
                print("Rollnumber cannot contain more than 10 characters")
            if  not rollnumber.isdigit():
                print("Rollnumber cannot contain letters")
            if  not firstname.isalpha():
                print ("First name cannot contain numbers")
            if  not lastname.isalpha():
                print("Last name cannot contain digits")
            continue
   
    unique_code = firstname[:4].upper() + lastname[:3].lower() + rollnumber[-3:]
    print("Your unique code is: ", unique_code)

verification_process()
