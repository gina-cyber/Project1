# This is a guess the number game.
import random

class Guessing_Game:
    def __init__(self):
      print(“Welcome to Numbers Guessing Game!!!”)
      solution = random.randint(1,10)
    
      Number_Of_Guess = 5
      Attempts = 0
    
      while Attempts < Number_Of_Guess:
        Attempts=Attempts+1
        print("Take a guess at a number between 1 and 10:") 
        guess = int(input())
    
        if guess < solution:
          print("try guessing higher")
        elif guess > solution:
          print("try guessing lower")
        else:
          print(f'Good job. It took {Attempts} attempts!') 

Guessing_Game()
