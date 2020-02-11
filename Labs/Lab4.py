""" Guessing Game """
import random
answer = random.randint(1, 1000)


class Colors:
    green = '\033[32m'


def guessing_game(answer):
    x = False
    first = 0
    last = 1000
    number_of_guess = 0
    while not x:
        try:
            guess = int(input())
            if guess < first or guess > last:
                x = False
                print(f"Pleas enter number from range {first, last}!")
            elif guess < answer:
                number_of_guess += 1
                x = False
                first = guess + 1
                print(f"Try again! This was your {number_of_guess} guess.\nTry another number from range {first, last}:")
            elif guess > answer:
                number_of_guess += 1
                x = False
                last = guess - 1
                print(f"Try again! This was your {number_of_guess} guess.\nTry another number from range {first, last}:")
            else:
                x = True
        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Please enter a number!")
        except KeyboardInterrupt:
            print("\nNo input taken.\n")
            pass

    print(Colors.green + f"CONGRATS! You guessed it right! It took you {number_of_guess} guess(es)!")
    exit(1)


print("Guess number from 1 to 1000:")
print(guessing_game(answer))


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game(answer)



