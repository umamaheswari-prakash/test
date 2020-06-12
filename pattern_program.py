import math
num_rows=int(input("enter the no of rows:"))
if num_rows%2 ==0:
    print('enter a valid odd number')
else:
    k=1
    num = num_rows/2
    upper = math.ceil(num)
    for rows in range(0,upper):
       for coloumn in range(k):
           print("*", end=" ")
       k=k+2
       print()
    k=k-4
    for rows in range(0,upper):
       for coloumn in range(k):
           print("*",end=" ")
       k=k-2
       print()




