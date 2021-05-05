def ask():
    while True:
        try:
            number = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Thank you, your number squared is: {}".format(number**2))
            break

ask()