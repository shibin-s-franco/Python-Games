from art import logo
import random
import os

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def clear():
    _=os.system('cls')
        
def blackjack():
    clear()
    print(logo)
    player_cards=[]
    computer_cards=[]
    player_score=0
    computer_score=0
    for n in range(2):
        player_random_card=random.choice(cards)
        player_score += player_random_card
        player_cards.append(player_random_card) 
        computer_random_card=random.choice(cards)
        computer_score += computer_random_card
        computer_cards.append(computer_random_card)
    print(f"Your Cards:{player_cards},Current Score:{player_score}")
    print(f"Computer's First Card:{computer_cards[0]}")

    should_continu=True
    
    while should_continu:
        new_card=input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card=='y':
            should_continu=True
            player_random_card=random.choice(cards)
            player_score+=player_random_card
            player_cards.append(player_random_card)
            if 11 in player_cards and player_score>21:
                pos=player_cards.index(11)
                player_cards[pos]=1
                player_score-=10
            print(f"Your Cards:{player_cards},Current Score:{player_score}")

            

            if player_score>21:
                print(f"Computer's Final Hand:{computer_cards},Final Score:{computer_score}")
                print("You went over.You Lose")
                should_continu=False
           
            else:
                print(f"Computer's First Card:{computer_cards[0]}")
                
                
        else:
            while computer_score<17:
                computer_random_card=random.choice(cards)
                computer_score+=computer_random_card
                computer_cards.append(computer_random_card)
            should_continu=False
            print(f"Your Final Hand:{player_cards},Your Final Score:{player_score}")
            print(f"Computer's Final Hand:{computer_cards},Final Score:{computer_score}")
            if computer_score>21:
                print("You win")
            elif player_score>computer_score:
                print("You Win")
            elif player_score==computer_score:
                print("Draw")
            else:
                print("You Lose")
            if(input("Do you want to play a game of BLACKJACK? type 'y' or 'n'"))=='y':
                blackjack()

        

    
if(input("Do you want to play a game of blackjack?Type 'y' or 'n'")=='y'):
    blackjack()
