#Kindly do the following on lists and I hope you learnt the list functions as I sent the slides on LMS last week. We are starting strings.
def random(number):
    # Remove the x parameter since we're getting input inside the function
    return number + number

result= random(5)
print(result)

def message(name):
    print(f"Welcome to code.{str(name)}")

def describe_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe_person(name="Jamon", age=19, country="Nigeria")
