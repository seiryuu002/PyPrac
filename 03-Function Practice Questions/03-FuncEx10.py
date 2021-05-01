def summer_69(mylist):
    total = 0
    add =True
    for i in mylist:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
