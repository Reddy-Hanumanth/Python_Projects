import random
n = random.randint(1, 100)
a = -1
guesses = 1

while(a != n):
    a = int(input("Guess a Number: "))
    if(a > n):
        print("Lower Number Please")
    elif(a<n):
        print("Heigher Number please")
    guesses +=1


print(f"You guessed correct number:{n} in {guesses} atempts")