f=open("C:/Users/Lenovo-PC/Desktop/New folder/sample.txt",'a')
f.write("dept: BE-ECE")
f.close()
f=open("C:/Users/Lenovo-PC/Desktop/New folder/sample.txt",'r')
print(f.read())
count =0
fp =open("C:/Users/Lenovo-PC/Desktop/New folder/sample.txt")
for line in fp:
    count += 1
    print((line.strip()))