# method 1 
def unique_list(mylist):
    mylist = list(set(mylist))
    print(mylist)

# method 2
def unique_list2(mylist):
    seen_numbers = []
    for num in mylist:
        if num not in seen_numbers:
            seen_numbers.append(num)
    print(seen_numbers)

unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
unique_list2([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
