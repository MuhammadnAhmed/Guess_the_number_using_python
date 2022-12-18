# Created by Muhammad Ahmed
# Checkout my Portfolio https://a03152049334.wixsite.com/muhammadahmed
# Checkout my Fiverr account https://www.fiverr.com/ahmed189
# Checkout my Upwork account https://www.upwork.com/freelancers/~01e248930a029b5290
# Follow me on LinkedIn http://www.linkedin.com/in/muhammad-ahmed189
# Follow me on GitHub https://github.com/MuhammadnAhmed


import random

# Function to guess the number

def guess_number():

    # initialize the randon number between 1 and 10
    randon_number = random.randint(1, 10)
    guess = 0

    # loop will check if number is correct or not
    while guess != randon_number:
        guess = int(input("Guess the number between 1 and 10 : "))

        # gives the clue if guessed number is smaller than the actual number
        if guess < randon_number:
            print("Unfortunately your guess is less than the actual number. Guess again!")
        # gives the clue if guessed number is larger than the actual number
        if guess > randon_number:
            print("Unfortunately your guess is greater than the actual number. Guess again!")

    print(f"Congrats! You guessed the number {randon_number} right!")


guess_number()
