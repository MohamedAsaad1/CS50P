import random

def main ():
    level = check("Level:")
    ren = random.randint(1, level)
    guess = check("Guess:")
    same_random(ren, guess)




def check(string):
    while True :
        try:
            guess = int(input(string))
            if guess > 0:
                return guess
        except ValueError:
            pass

def same_random(random , guesses):
    while True:

        if guesses > random:
            print("Too large!")
            guesses = check("Guess:")

        elif guesses < random:
            print("Too small!")
            guesses = check("Guess:")

        else:
            print("Just right!")
            exit()



main()