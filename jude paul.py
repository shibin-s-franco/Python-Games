#print('
print("Welcome To The Adventure Of Jude Paul")
action1=input("I Jude Paul wake up and decided to __________ (do nothing/opened)") 
action1=action1.lower()
if action1=="do nothing":
    print("do nothing.THE END")
else:
    action2=input("he opened his drawer and took a________ (red/blue)")
    action2=action2.lower()
    if action2=="red":
        print("red can of poison,drink it and died.THE END")
    else:
        action3=input("blue ipad and open __________(instagram/mail)")
        action3=action3.lower()
        if action3=="instagram":
            print("watched reels and spend his day using instagram and playing games.THE END")
        else:
            print("mail and find out he is the new CEO of google.Then he decided to bring some changes to the youtube.And started working.YOU WIN")

print("CONTINUATION ON PART TWO")