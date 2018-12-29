import random
import time
import sys
import os


def get_lowest_number(high_score, number_of_tries):
    if high_score == 0:
        high_score = number_of_tries
    elif number_of_tries < high_score:
        high_score = number_of_tries
    return high_score


def clear_screen():
    time.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")


def roll_out():
    time.sleep(.55)
    print("-----------------------------------------")
    time.sleep(.55)


def start_game():
    correct_guess = random.randint(1, 21)
    number_range = list(range(1, 21))
    number_of_tries = 0
    high_score = 0


    roll_out()
    print("  Welcome to the Numbers Guessing Game.")
    roll_out()

    while True:
        try:
            roll_out()
            player_guess = int(input("\nPick a number between 1 and 20:\n"))
        except ValueError:
            print("\nOh no, Invalid input. Please try again")
            print("Number must be between 1 and 20")
            continue
        if player_guess > correct_guess:
            number_of_tries +=1
            print("\nTry again! The number you picked is higher")
        elif player_guess < correct_guess:
            number_of_tries +=1
            print("Try again! The number you picked is lower")
        elif player_guess == correct_guess:
            number_of_tries +=1
            print(f"\nThat's correct! It took you {number_of_tries} tries!")
            while True:
                replay = input("\nWould you like to play again? (Y/N)\n")
                if replay.upper() == 'Y':
                    correct_guess = random.randint(1, 21)
                    high_score = get_lowest_number(high_score, number_of_tries)
                    roll_out()
                    print(f"\tThe current highscore is {high_score}")
                    roll_out()
                    number_of_tries = 0
                    clear_screen()
                    break
                elif replay.upper() == 'N',:
                    roll_out()
                    print("\t\tGAME OVER!!\n\t    Thanks for playing!")
                    roll_out()
                    clear_screen()
                    sys.exit()
                #replay = input("\nWould you like to play again? (Y/N)\n")


if __name__ == '__main__':
    start_game()
