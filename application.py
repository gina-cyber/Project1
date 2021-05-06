# This is a guess the number game.
import random

def start_game():
    print("Welcome to Numbers Guessing Game!!!")
    solution = random.randint(1,10)
   
    Number_Of_Guess = 5
    Attempts = 0
    got_answer = False
    while Attempts < Number_Of_Guess:
        print("Take a guess at a number between 1 and 10:")
        try:
            guess = int(input())
            if (guess < 1 or guess > 10):
                print("Must enter nubmer between 1 and 10")
                continue
        except ValueError:
         print("Must enter a whole number:")
         continue
   
        Attempts = Attempts+1
        if guess < solution:
            print("try guessing higher")
        elif guess > solution:
            print("try guessing  lower")
        else:
            print(f'Good job. It took {Attempts} attempts to guess {solution}!')
            got_answer=True
            break
            
    if (got_answer==False):
            print(f'Sorry, you guessed the max times {Attempts}. Try playing again')
       
def end_game():
     print("Game ends here.")
        
if __name__ == "__main__":
    start_game()
    end_game()
