from art import logo,vs
from game_data import data
import random
from os import system, name
  

  
# define our clear function
def clear():    
    # print(system('cls'))
    system('cls')
  
def random_account():
    """"give a random account directory from the data list"""
    return random.choice(data)

def account_details(acc):
    """Return the  follower_count value in a dict"""
    return acc["follower_count"]

def compare_acc_follower(accA,accB):
    """"Compare two dict and gives the name of the account with higher followers"""
    if accA['follower_count']>accB['follower_count']:
        return 'a'
    else:
        return 'b'

def replace(accA,accB):
    """Compare two dict and gives the dict with more followers"""
    accA_follower=account_details(accA)
    accB_follower=account_details(accB)
    if accA_follower>accB_follower:
        return accA
    elif accA_follower<accB_follower:
        return accB 

continue_game=True
score=0
print(logo)
acc_A=random_account()
acc_B=random_account()


while continue_game:
    if acc_A==acc_B:
        acc_B=random_account() 
     
    print("Compare A:{name},a {description},from {country}".format(**acc_A))
    print(vs)
    print("Compare B:{name},a {description},from {country}".format(**acc_B))
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    more_follower=compare_acc_follower(acc_A,acc_B)
    
    if guess==more_follower:
        score+=1
        acc_A=replace(accA=acc_A,accB=acc_B)
        acc_B=random_account()
        clear()
        print(logo)
        print(f"You're right!Current Score: {score}")
           
    else:
        clear()
        print(logo)
        print(f"Sorry,that's wrong.Final Score: {score}")
        continue_game=False

