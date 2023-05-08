import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#Step 1

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

#Step 4

#TODO-8: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for char in chosen_word:
#     if guess == char:
#         print("Right")
#     else:
#         print("Wrong")

#Step 2

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for char in chosen_word:
    display.append("_")

#Step 3

#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False

# while '_' in display:
while not end_of_game:
    guess = input("Guess a letter: ")


#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = letter

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    print(display)    

    #TODO-9: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
    
    if lives == 0:
        print("You lose.")
        end_of_game = True

  
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-10: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

#Step 5


# from hangman_art import logo

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]


#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.



#Testing code


#Create blanks


    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    

    #Check guessed letter
    
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        

    #Check if user is wrong.
    
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        

    #Join all the elements in the list and turn it into a String.
    

    #Check if user has got all letters.
    

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    