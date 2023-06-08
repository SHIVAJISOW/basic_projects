import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"what is the random number you want to type {x} "))
        if guess> random_number:
            return "sorry the guess was very high "
        elif guess < random_number:
            return "guess was very low "

    print(f"yes you have guessed the right number {x}")

def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high :
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess} is too high (h) or too low(l) or it is correct (c)").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1

    print("yes computer guessed the number correctly ")


computer_guess(100)
