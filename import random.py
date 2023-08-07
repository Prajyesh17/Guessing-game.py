import random

generated_number = random.randint(1,100)
print(generated_number)

guess = 0 

while guess != generated_number:
    guess = int(input("whats your guess"))

    if guess < generated_number:
        print("Too low")
    elif guess > generated_number:
        print("little high")

    else: print("you got it")
