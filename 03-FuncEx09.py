def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a, b, c))
    elif a == 11 or b == 11 or c ==11:
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7)) 
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
