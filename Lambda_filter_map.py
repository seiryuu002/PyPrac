# we use map function when we want to call any specific 
# for more than one items, when we don't want to apply 
# for loop
 
def squares(nums):
    return nums**2

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]        # our list

another_list = list(map(squares, mylist))   # we convert all the output in a list

print(another_list)                         # print resulting list

# we can also iterate thru map()
# it will also produce same result

for n in map(squares, mylist): # notice we don't call function squares() 
    print(n)                   # we just pass the name function as an 
                               # argument


# filter function :- we use this function to filter out desired output

def is_even(num):
    return num%2 == 0

print(list(filter(is_even, mylist)))      # filter is similar to but it is
                                          # used to give output only if 
                                          # conditions are true
# we can also itereate thru filter in similar as map function

# Lambda expressions
mylists = list(map(lambda x : x**2, mylist)) # we use lambda expression when we need 
print(mylists)                               # function for just one time or we need 
                                             # anonymous function 