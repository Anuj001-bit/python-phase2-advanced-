a  = int(input("Enter a number : "))

table = [a*i for i in range(0,11)]

with open("table.txt", "a") as f :
    f.write(f" Table of {a} is {str(table)}  \n")



