beer=10
pork=30
age= int(input("How old are you?"))

if age >= 18:
    pretax = beer + pork
    tax = pretax * 0.05
    total = pretax + tax
    print("Your total is", total)

else:
    print("You are under 18, you cant buy beer.")
    print("Your total is", pork)