print("Runner 1:")
name1=input("Name:")
time1=float(input("Time (in seconds):"))
print("Runner 2:")
name2=input("Name:")
time2=float(input("Time (in seconds):"))

if time1>time2:
    print(f"The faster runner is:{name1}")
elif time1<time2:
    print(f"The faster runner is:{name2}")
else :
    print(f"{name1} and {name2} have the same time")