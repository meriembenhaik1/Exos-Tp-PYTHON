temp=int(input("Please type in the temperature:"))
if temp<=0:
    print("It's freezing!")
    print("It's cold!")
    print("It's cool!")
    print("Stay safe!")
elif temp>0 and temp <=10:
    print("It's cold!")
    print("It's cool!")
    print("Stay safe!")
elif temp>10 and temp <=20:
    print("It's cool!")
    print("Stay safe!")
else:
    print("Stay safe!")

