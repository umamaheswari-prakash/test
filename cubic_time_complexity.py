rows = int(input("Enter the no of rows: "))
for row in range(1,rows):
    for row in range(0,row,1):
        print(format(2**row,"4d"), end=" ")
    for row in range(-1+row,-1,-1):
        print(format(2**row, "4d"), end="")
    print("")
