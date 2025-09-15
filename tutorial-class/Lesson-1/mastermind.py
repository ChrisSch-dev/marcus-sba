import random

digits = "0123456789"

# Randomply generate 4 numbers
code = random.sample(digits, 4) # <- list
print(code)
while True:
    # Task 1: Get input from user ans store in variable guess
    guess = input('please input 4 numbers eg.(1234):')

    if guess.isdigit() and len(guess) == 4: # Task 2: Determine if the user's input is a number, and if it is in four-digit
        check = ""

        # Check if the guess is correct
        for i in range(4):
            # Task 3: Complete the if condition, Determine if the number is in the correct position
            # Hints: code[i] represents the i-th number of the code, guess[i] represents the i-th number of the guess
            if guess[i] == code[i]:
                check = check + "O"
            # Task 4: Complete the elif condition, Determine if the number is exist, but in the wrong position
            elif guess[i] in code :
                check = check + "?"
            else:
                check = check + "X"
        print("Your guess is:", check)

        # Task 5: Determine if the guess is correct
        # Hints：What is value of check should be if the guess is correct
        if guess == "".join(map(str, code)):
            print("You win!")
            break
    else:
        print("Invalid guess")
