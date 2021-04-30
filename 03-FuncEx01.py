def lesser_of_two_events(a, b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_events(2,4))
print(lesser_of_two_events(2, 5))
print(lesser_of_two_events(3, 5))
print(lesser_of_two_events(10, 11))
