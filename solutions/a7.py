# how to create a global variable
some_variable = 10

def some_method():
    global some_variable
    print(some_variable) # can access it
    some_variable=1 # can change it
    print(some_variable)

some_method()