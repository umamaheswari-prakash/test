minimum=int(input("enter the minimum value:"))
maximum=int(input("enter the maximum value:"))
print("number divide by both 75 and 100:")
for i in range(minimum,maximum+1):
  if i%75==0 and i%100==0:
      print(i)


