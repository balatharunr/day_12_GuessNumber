import random
import art
print(art.logo)

print("Welcome to Number guessing Game:\n")
print("I'm thinking of a number between 1 to 100: ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = int(random.randint(1, 20) * 5)
guess = 1

def find():
    global guess, number
    guess = int(input("Make a guess: "))
    if guess != number:
        if number > guess:
            print("Too Low")
        else:
            print("Too High")
        return False
    else:
        return True

def process(n):
    print(f"You have {n} attempts remaining to guess the number\n")
    while n >= 1:
        found = find()
        n -= 1
        if found:
            print("You Win, Number found!!")
            break
        else:
            print(f"You've {n} attempts")
    if n == 0:
        print("You've run out of guesses, you lose!")

if difficulty == "hard":
    process(5)
else:
    process(10)
