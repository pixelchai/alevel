import random

SEPARATOR = "------------------------------------"

# task 1
print("Hello, "+input("Please enter your name: "))
print(SEPARATOR)

# task 2
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print(num1+num2)
print(SEPARATOR)

input("press enter to continue")

# task 3
for i in range(13):
    print(str(i)+" times tables: ")
    for j in range(13):
        print(str(i)+"x"+str(j)+"=="+str(i*j))
    input("press enter to continue")

print(SEPARATOR)

# task 4
# todo
print("todo")

print(SEPARATOR)

# task 5
attempts_limit=10
attempts=1
num=random.randint(0,100)
print("My number is between 0 and 100. Try guess it.")
while True:
    guess=int(input("Enter a guess: "))
    if attempts>=attempts_limit: # extension
        print("You ran out of attempts")
        break
    if guess>num:
        print("Too high~")
    elif guess<num:
        print("Too low~")
    else:
        print("Yep~")
        print("It took you " + str(attempts) + " attempts")
        break
    attempts+=1
input("press enter to continue")

# task 6
print(''.join(list(reversed(input("Enter a string to reverse: ")))))