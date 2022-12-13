# Number guessing game

import random as r

num = r.randint(0,100)
attempt = 10
print('Number Guessing Between 0 & 100')

for i in range(attempt):
    value = int(input("\nEnter your guess : "))

    if num == value:
        print("Congratulations, You Are Winner !")
        break
    elif num > value:
        print("Number Is Above Your Guess")
    else:
        print("Number Is Below Your Guess")

    print(f"{attempt-(i+1)} Attempts Left")

else:
    print("You Have Reached Your Last Attempt\nYou Are Looser")