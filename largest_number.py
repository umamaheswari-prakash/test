def Max(inum):
    x = [0 for x in range(10)]
    string = str(num)
    for i in range(len(string)):
        x[int(string[i])] = x[int(string[i])] + 1
    ans = 0
    val= 1
    for i in range(10):
        while x[i] > 0:
            ans= ans+ (i * val)
            x[i] = x[i] - 1
            val = val* 10
    return ans
num = input("enter a number: ")
print (Max(num))