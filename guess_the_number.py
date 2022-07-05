import random


print(  """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")
print("Welcome to the number Guessing Game")
number=random.randint(1,100)
# print(f"The answer is {number}")
if(input("Choose a diffeculty type? 'easy' or 'hard':")=="easy"):
    lives=10
else:
    lives=5
while not lives==0:
    print(f"You have {lives} attempts remaining to guess the number")
    guess=int(input("Make a guess"))
    if guess==number:
        print(f"You got it,the answer was {number}")
    else:
        lives-=1
        if guess>number:
            print("Too High")
        elif guess<number:
            print("Too Low")
        if lives==0:
            print(f"You Lost.You have ran out of live,the answer was {number}")