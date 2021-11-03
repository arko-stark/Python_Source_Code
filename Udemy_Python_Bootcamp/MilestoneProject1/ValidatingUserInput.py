def user_choice():
    # initial choice
    choice = 'WRONG'
    accetable_range = range(0,11)
    within_range = False

    # two conditions to check
    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter a number (0-10) :')
        if int(choice) in accetable_range :
            within_range = True

    return int(choice)

print (user_choice())