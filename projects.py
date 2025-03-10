import random
game_rule = ["stone" , "paper" , "scisser"]
user_choice = int(input("enter your choice, you choose 1.stone, 2.paper and 3.scisser \n"))
print(game_rule[user_choice])
computer_choice = random.randint(0,2)
print(game_rule[computer_choice])
if user_choice == computer_choice:
    print("match draw!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif user_choice == 2 and computer_choice == 0:
    print("you lose!")
elif  computer_choice > user_choice :
    print("you lose!")
elif computer_choice < user_choice:
    print("you win")
else:
    print("enter a valid input")
    
