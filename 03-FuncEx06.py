def almost_there(n):
    if 90 <= n <= 110:
        return True
    elif 190 <= n <= 210:
        return True
    return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

    
