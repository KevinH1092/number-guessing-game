import random

print("""This is the number guessing game!
         Guess the correct number between 1-100!
          You have seven tries. Please only enter integers!""")

# Generate the random number
num = random.randrange(1,100)

counter = 0
while counter < 7 :
    guess = int(input("Guess a number: "))
    counter += 1
    if num == guess:
        print("Congrats! You guessed", num, "in", counter, "attempts.")
        break
    elif counter >= 7:
        print("Sorry, you didn't guess the correct number in 7 attempts. Try again!")
        break
    elif num > guess:
        print("Your number is too small, try again!")
    elif num < guess:
        print("Your number is too large, try again!")



