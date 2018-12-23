import random
import time


def roll_out():
    time.sleep(.6)
    
def start_game():
    correct_guess = random.randint(1, 21)
    number_range = list(range(1, 21))
    number_of_tries = 0
    
    roll_out()
    print("-------------------------------------")
    roll_out()
    print("Welcome to the Numbers Guessing Game.")
    roll_out()
    print("-------------------------------------")
    
    while True:        
        number_of_tries +=1
        try:
            roll_out()
            player_guess = int(input("\nPick a number between 1 and 20:\n"))
            if player_guess not in number_range:
                raise ValueError("Number must be between 1 and 20")
        except ValueError as err:
            print("Oh no, Invalid input. Please try again")
            print(f"{err}")
            continue
        if player_guess > correct_guess:
            print("\nTry again! The number you picked is higher")
        elif player_guess < correct_guess:
            print("Try again! The number you picked is lower")    
        elif player_guess == correct_guess:
            print(f"\nThat's correct! It took you {number_of_tries} tries!")
            replay = input("\nWould you like to play again? (Y/N)\n")
            if replay.upper() == 'Y':                
                roll_out()
                print("-----------------------------------------")
                roll_out()
                print(f"\tThe current highscore is {high_score}")
                roll_out()
                print("-----------------------------------------")
                roll_out()
                number_of_tries = 0
                continue
            else:
                roll_out()
                print("-----------------------------------------")
                roll_out()
                print("\t\tGAME OVER!!\n\t    Thanks for playing!")
                roll_out()
                print("-----------------------------------------")
                break         
            
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
