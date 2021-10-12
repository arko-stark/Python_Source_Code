# shuffling game ball
from random import shuffle


def shuffle_list(mylist) :
    shuffle(mylist)
    return mylist
def player_guess():
    guess = ''
    while guess not in ['1','2','3']:
        guess = input('There are 3 buckets, Guess which bucket the ball is in : ')
    return int(guess)
def check_guess(shuffled_list,player_guess):
    if shuffled_list[player_guess-1] == 'O':
        print('Its a match...You Won!')
        print(shuffled_list)
    else :
        print('No Match ! Try again')
        print(shuffled_list)

# setting the initial list
cup_bucket = [' ','O','']


#shuffling the list
new_list = shuffle_list(cup_bucket)

#get player guess
new_guess = player_guess()

#check if it is a match
check_guess(new_list,new_guess)


