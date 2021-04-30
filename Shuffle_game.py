from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def guess():
    myguess = ''
    while myguess not in ['0', '1', '2']:
        myguess = input("pick a number between 0-2:")
    return int(myguess)


def check_guess(mylist, myguess):
    if mylist[myguess] == '0':
        print("correct")
    else:
        print("wrong guess")
        print(mylist)

mylist = [' ', '0', ' ']
mixed_list = shuffle_list(mylist)
myguess = guess()
check_guess(mixed_list, myguess)

