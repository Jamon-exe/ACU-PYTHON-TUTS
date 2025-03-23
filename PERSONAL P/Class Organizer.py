
condition = 'yes'
while condition == 'yes':
    name= input('Enter your name:')
    print(f'Hello {name}! Welcome to the class organizer.')
    print('Please enter the following details:')
    course = input('Enter the course you are taking:')
    if course == 'Python':
        print('What week do you want to see')
        week = int(input('Enter the week number:'))
        if week == 1:
            print(' You learnt basic python programming (no code/move to the next week)')
        elif week == 2:
            print('you learnt how to print helloword')
            week2_runstatus = input('Did you run the code? (yes/no):')
            if week2_runstatus == 'yes':
                print ("This was the code: \n \n Hello World, class dey be\n2\nThe boy is going to school. Code: print  (Hello World, class dey be\n 2 \n The boy is going to school.)")
            else:
                print('Alright')
            
    elif course == 'HTML':
        print('What week do you want to see')
    condition=input('Do you want to continue? (yes/no):')