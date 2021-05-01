def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1+n2 == 20


print(makes_twenty(20, 20))
print(makes_twenty(21, 21))
print(makes_twenty(20, 21))
print(makes_twenty(18, 2))
