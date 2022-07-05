import os
clear=lambda:os.system('cls')
from hangman_ascii import stages,logo
from hangman_words import word_list
import random

print(logo)
chosen_word=random.choice(word_list)
# print(f"the solution is {chosen_word}")
display=[]
chosen_word_length=len(chosen_word)
for i in range(chosen_word_length):
    display.append("_")
# print(display)
lives=0
end_of_game=False
while not end_of_game :
    guess=(input("Guess a letter ")).lower()
    clear()
    position=0
    if guess in chosen_word: 
        if guess in display:
            print(f"You have already gussed {guess} ")
        for letter in chosen_word:
            position+=1
            if letter == guess:
                display[position-1]=letter
        
    else:
        print(f"You Guessed {guess} thats not in the word,You lose a live")
        lives+=1

    print(stages[lives])
    print(f"{''.join(display)}" )

    if not '_' in display:
        end_of_game=True
        print("You Win") 
     
    if lives==6:
        end_of_game=True
        print("You Lose")
    