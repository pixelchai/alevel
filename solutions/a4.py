# definite iteration
for i in range(10):
    print(i)

# indefinite iteration
i=0
while True:
    if i==10: break
    print(i)
    i+=1

# nested loop
for i in range(13):
    print(str(i)+" times tables: ")
    for j in range(13):
        print(str(i)+"x"+str(j)+"=="+str(i*j))
    input("press enter to continue")