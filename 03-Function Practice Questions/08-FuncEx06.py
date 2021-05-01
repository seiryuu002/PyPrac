def palindrome(string):
    string = string.replace(" ","")
    new_string = string[::-1]
    print(string == new_string)


palindrome('helleh')
