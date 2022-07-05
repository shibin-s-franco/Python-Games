import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''
paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''
scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

#Choice Display

player_choice=int(input("What Do you choose?Type 0 for Rock,1 for Paper,2 for Scissors"))
if player_choice>=3 or player_choice<0:
    print("You type an invalid input,You Lose" )
    exit()
game=[rock,paper,scissors]
print(game[player_choice])
computer_choice=random.randint(0,2)
print("Computer Chose:")
print(game[computer_choice])

#Game Logic

if player_choice == computer_choice:
    print("Draw")
elif player_choice == 0 and computer_choice == 1:
    print("You Lose")
elif player_choice == 0 and computer_choice == 2:
    print("You Win")
elif player_choice == 1 and computer_choice == 0:
    print("You Win")
elif player_choice == 1 and computer_choice == 2:
    print("You Lose")
elif player_choice == 2 and computer_choice == 0:
    print("You Lose")
elif player_choice == 2 and computer_choice == 1:
    print("You Win")