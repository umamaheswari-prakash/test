dictionary={"Spain":"Europe","Japan":"Asia","India":"asia","Italy":"Europe","Thailand":"Asia","Sudan":"Africa"}
val=input("enter the continent:")
print("country name:")
for key,value in dictionary.items():
    if val.upper() == value.upper():
        print(key)
