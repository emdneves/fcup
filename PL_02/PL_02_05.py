import math

value = int(input("insert value "))

bills =[20, 10, 5, 1]
num_bills = [0, 0, 0, 0]

for i in range(len(bills)):
    num_bills[i] = value // bills[i]
    value = value % bills[i]

for i in range(len(bills)):
    print(str(bills[i]) + " : " + str(num_bills[i]))