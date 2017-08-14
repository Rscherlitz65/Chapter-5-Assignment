# Ryan Scherlitz
# ISYS 110
# 3/2/2017
import random

# Define variables

user_guess = 0
upper_limit = 100
lower_limit = 1
ai_number = 0

# -----AI generates a random number-----#
ai_number = random.randint(1, 100)


# -----Users guess as to what the number is-----#
def guess():
    x = int(input("Guess A number between 1 and 100: "))
    return x


def compare(x, y, z, ai):
    if x <= y <= z:
        if y < ai:
            print("Your guess is too low, try again")
            print("The number was", ai_number)
            main()
        elif y > ai:
            print("Your guess is too high, try again")
            print("The number was", ai_number)
            main()
        elif y == ai:
            print("Congratulations!")
            print("You solve it in", "attempts")
            print("The number was", ai_number)

    else:
        print("Your guess is out of range, try again")
        print("The number was", ai_number)
        main()
    return


def main():
    user_guess = guess()
    compare(lower_limit, user_guess, upper_limit, ai_number)


main()