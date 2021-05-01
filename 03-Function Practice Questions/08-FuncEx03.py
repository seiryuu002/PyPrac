def up_low(string):
    upcase = 0
    lowcase = 0
    print(' ')
    print(' ')
    for i in string:
        if i.isupper():
            upcase += 1
        elif i.islower():
            lowcase += 1
        else:
            pass    
    print(f"Original string : {string}")
    print(f'No. of upper case characters: {upcase}')
    print(f'No. of lower case characters: {lowcase}')
    print(' ')
    print(' ')
    return 0



s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
