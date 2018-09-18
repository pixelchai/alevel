# higher or lower game was already implemented in task 5
# extending it to play itself:
# this is the best AI possible:
import random

attempts=1
num=random.randint(0,100)
print("My number is between 0 and 100. Try guess it.")
while True:
    print("Enter a guess: "+str(num))
    guess=num
    if guess>num:
        print("Too high~")
    elif guess<num:
        print("Too low~")
    else:
        print("Yep~")
        break
    attempts+=1
print("It took you "+str(attempts)+" attempts")