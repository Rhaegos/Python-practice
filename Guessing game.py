#Guessing game 1 exercise
import random
import sys

guess = int()

while True:
  guess_count = 0
  secret_num = random.randint(1,9)
  cont = input("Welcome to the guessing game. The secret number is any number from 1 to 9!\nType exit to exit or anything else to continue: ")
  if cont == "exit":
    sys.exit("Thanks for playing!")
  while guess != secret_num:
    guess = int(input("Enter your guess: "))
    if guess == secret_num:
      print("You have the correct guess!\nYou took " + str(guess_count) + " tries!")
    elif guess > secret_num:
        print("Your guess is too high, try again")
    elif guess < secret_num:
        print("Your guess is too low, try again")
    guess_count = guess_count + 1
print("Thanks for playing!")