#day 3 coding challenge
# I write prototype simple auto service station with logic operators if, elif, else
import random


print("Welcome to the auto service station.")

print('''              ______--------___
             /|             / |
  o___________|_\__________/__|
 ]|___     |  |=   ||  =|___  |"
 //   \\    |  |____||_///   \\|"
|  X  |\--------------/|  X  |\"
 \___/  Auto service   \___/
 ''')


ask = input('What are you problem? Is you car broke down? (Yes, No)')
if ask == 'Yes':
    problem = input('Do you know what broke down in your car? (Yes, No)')
    if problem == 'Yes':
        print('OK, We will making diagnostic')
        diagnostic = random.randint(0, 1)
        if diagnostic:
            print('You are right, we will repairing your car after 30 minutes')
            print('You car repaired, have a good day')
        else:
            print('You are not right, we find other defect')
            print('Searching spare parts... please wait')
            print('We find it, Lets start to repairing your car')
            print('You car repaired, have a good day')
    elif problem == 'No':
        print('OK, we will making diagnostic, please waiting...')
        print('We found defect in your car')
        print('Searching spare parts... please wait')
        print('We find it, Lets start to repairing your car')
        print('You car repaired, have a good day')
    else:
        print('Have a good day')

elif ask == 'No':
    reglament = input('You are wanting maintenance works? (Yes, No)')
    if reglament == 'Yes':
        print('OK, We will making it... please waiting...')
        print('You car repaired, have a good day')
    else:
        print('Have a good day')




