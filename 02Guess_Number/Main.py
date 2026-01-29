
import random
n = random.randint(1, 100)
a = -1
guesses = 1
try:
    while(a != n):
        a = int(input("Guess a Number: "))
        if(a > n):
            print("Lower Number Please")
        elif(a<n):
            print("Heigher Number please")
        guesses +=1
except ValueError:
    print("Please Enter a Valid Number")
else:
    print(f"You guessed correct number:{n} in {guesses} atempts")