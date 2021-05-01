def animal_crackers(text):
    string = text.upper().split()
    return string[0][0] == string[1][0]


print(animal_crackers("Levelheaded llama"))
print(animal_crackers("Crazy Kangaroo"))
