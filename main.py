import json
import random
from collections import Counter

# OPENING JSON FILES REQUIRES THE READ BINARY RECURSIVE STRATEGY
def load_json(filename):
    with open(filename, "rb") as json_file:
        data = json.load(json_file)
        json_file.close()

        if data: return data
    return []

def bubbleSort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j]["word"] < list[j + 1]["word"]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

def binarySearch(list, target):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2

        if list[mid]["word"].lower() == target.lower():
            return list[mid]
        else:
            if target.lower() > list[mid]["word"].lower():
                end = mid - 1
            else:
                start = mid + 1
    return None

def getProperCount(guess, word):
    correct_count = Counter(word)

    guess = guess.ljust(len(word))
    correct_word = [w if guess[k] != w else None for k, w in enumerate(word)]

    concatenateString = ""

    for k in range(len(guess)):
        letter = guess[k]
        tempString = "_"

        if letter and letter in word:
            if word[k] == letter:
                correct_count[letter] -= 1
                tempString = letter
            elif letter in correct_word and correct_count[letter] > 0:
                correct_count[letter] -= 1
                tempString = "?"
        concatenateString += tempString

    return concatenateString

def dictionary(list):
    sorted_list = bubbleSort(list)

    userInput = input("Please enter a word: ")

    find = binarySearch(sorted_list, userInput)

    if find is None:
        print("This word was not in the dictionary. Please try again.")

        input("Press Enter to continue...")

        return

    print("\n")
    print("Word Found Successfully:")
    print("Word: " + find["word"])
    print("Part of Speech:" + find["pos"])
    print("Chinese Definition: " + find["chinDef"])
    print("\n")

    input("Press Enter to continue...")

file = load_json("dict2.json")

def quiz(list):
    randomList = random.sample(list, 1)[0]

    print("\n")

    userInput = ""

    while len(userInput) != len(randomList["word"]):
        userInput = input("What is " + randomList["chinDef"] + " in English?\nThe answer has " + str(len(randomList["word"])) + " letters total\n\nYour answer: ")

    counting = getProperCount(userInput.lower(), randomList["word"].lower())

    while userInput.lower() != randomList["word"].lower():
        print("\n")
        userInput = input("That guess was wrong!" + "\n\n" + "What is " + randomList["chinDef"] + " in English?\nThe answer has " + str(len(randomList["word"])) + " letters total" + "\n\n" + "Here is a hint based on your last guess to help you guess the word: (? = incorrect position in last guess // _ = wrong placement in last guess)" + "\n" + counting + "\n\n" + "Your answer: ")

    if userInput.lower() == randomList["word"].lower():
        print("You guessed the word!")
        print("\n")
        input("Press Enter to continue...")

    print('\n')

if len(file) < 1:
    print("No data was loaded. Please ensure the correct path was configured.")
    exit()

while True:
    userSelect = input("Select a mode:\n\n1) Dictionary Mode\n2) Quiz Mode\n3) Exit Program\n\nYour choice: ")

    if not userSelect.isdigit() or userSelect not in ['1', '2', '3']:
        print("Invalid input. Please try again.")
        continue

    if userSelect == "1":
        dictionary(file)
    elif userSelect == "2":
        quiz(file)
    elif userSelect == "3":
        break
