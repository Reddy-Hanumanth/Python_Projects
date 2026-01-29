import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice (s/w/g): ")
youDict = {"s": 1, "w": -1, "g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    # if(computer == -1 and you ==1):     #-1 - 1 = -2
    #     print("you win!")
    # elif(computer == -1 and you == 0):  # -1
    #     print("you lose!")
    # elif(computer == 1 and you == -1):  # 2
    #     print("you lose!")
    # elif(computer == 1 and you == 0):   # 1
    #     print("you win!")
    # elif(computer == 0 and you == -1):  # 1
    #     print("you win!")
    # elif(computer == 0 and you == 1):   # -1
    #     print("you lose!")
    # else:
    #     print("Somthing went wrong!")


    if((computer - you) == -1 or (computer - you) == 2):
        print("you lose!")
    else:
        print("you win!")