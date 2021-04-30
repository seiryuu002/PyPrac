def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 20))
print(makes_twenty(21, 20))
print(makes_twenty(20, 21))
print(makes_twenty(18, 2))
