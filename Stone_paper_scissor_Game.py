#Stone paper scissor game in python by using random module
import random
a = ["r","p","s"]
print("Enter r for Rock")
print("Enter p for Paper")
print("Enter s for scissor")


i=0
player=0
cpu=0

while (i<10):
    b=random.choice(a)
    user_choice = input("\nEnter your choice : ")

    if(user_choice == 'r' or user_choice == 'p' or user_choice == 's'):
        print("Computer's Choise : ",b)

        if b==user_choice :
            print("It's a Tie")
        elif b=="r" and user_choice=="p" :
            print("You win")
            player += 1
        elif b=="r" and user_choice=="s" :
            print("You Lose")
            cpu+=1
        elif b=="p" and user_choice=="s" :
            print("You win")
            player+=1
        elif b=="p" and user_choice=="r" :
            print("You Lose")
            cpu+=1
        elif b=="s" and user_choice=="r" :
            print("You win")
            player+=1
        elif b=="s" and user_choice=="p" :
            print("You Lose")
            cpu+=1

        print("\nYour Score : ",player)
        print("Computer Score : ",cpu)
        print("------------------------------------------------------------------------------------")
        i = i + 1
    else :
        print("Invalid Choice")

print("your final Score is : ",player)
print("Computer's final Score is : ",cpu)

if player>cpu :
    print("-----------Congratuations,You won--------------------------------")
else:
    print("-----------Sorry,You Lose--------------------------------")