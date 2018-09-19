# exception handling
import traceback

try:
    num=input("Enter a numerator: ")
    denom=input("Enter a denominator: ")
    print("Evaluation: "+str(num/denom))
except TypeError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("FATAL ERROR")
    traceback.print_exc()