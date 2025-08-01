try:
    a = int (input("Enter your 1st number :"))
    b = int (input("Enter your 2nd number :"))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")

   
