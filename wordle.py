# Text-based "Wordle" game using basic Python
# Currently has some limitations and is not fool-proof
import random

def get_list():
    file = open("words.txt", "r")
    data = file.read()
    data_into_list = [x.strip() for x in data.split('\n')]
    file.close()
    return data_into_list

list_of_words = get_list()
# print(list_of_words)
num_tries = 6
choice = random.choice(list_of_words)
print(choice)

# Get a user guess input
def guess(): 
    guess = input("Enter a word: ")
    return guess

def split_to_char(word):
    return [char for char in word]

# Check that the user's guess is inthe list of words
def check_guess(guess, list_of_words):
    # First check if word is in the list
    guess_in_word = False # Default value of False
    if guess not in list_of_words:
        print("Guess not in list")
        return guess_in_word
    else:
        guess_in_word = True
        # print("word in list!")
        split_guess = split_to_char(guess)
        split_choice = split_to_char(choice)
        #print(split_guess)
        print(split_guess)
        for i in range(len(split_guess)):
            if split_choice[i] == split_guess[i]:
                print("✓", end = " ")
            elif (split_choice[i] != split_guess[i]) and (split_guess[i] in split_choice):
                print("*", end = " ")

            else:
                print("X", end = " ")

        print()

while num_tries > 0:
    for i in list_of_words:
        user_guess = guess()
        check_guess(user_guess, list_of_words)
        num_tries -= 1
        print("Number of guesses left: ", num_tries)
        if user_guess == choice:
            print("Correct!")
            num_tries = 0
            break
    


