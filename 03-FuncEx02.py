def animal_crackers(text):
    text = text.upper()
    string = text.split()
    if string[0][0] == string[1][0]:
        return True
    else:
        return False


print(animal_crackers("Levelheaded llama"))
print(animal_crackers("Crazy Kangaroo"))
