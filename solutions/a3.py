age=int(input("Age: "))
if age<16:
    print("You are too young to drive")
elif age<=16:
    print("You are old enough to ride a motorcycle")
elif age>=70:
    print("You need to requalify to drive a car")
else:
    print("You are able to drive in a license")
# python doesn't have case statements