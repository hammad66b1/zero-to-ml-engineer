num=7

while True:
    x=int(input("Enter your guess: "))
    if x>num:
        print("Number too high, guess again!")
        
    elif x<num:
        print("Number too short, guess again")
        
    else:
        break
print("Number guessed Correctly!")