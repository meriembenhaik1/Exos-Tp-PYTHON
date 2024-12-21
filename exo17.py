numbers=[]
shoe_sizes=[]
i=0
while i < 5:
    numbers.append(i + 1) 
    i += 1
print(numbers)
i=7
while i < 12:
    shoe_sizes.append(i + 1) 
    i += 1
print(shoe_sizes)

combined_list = numbers + shoe_sizes
print(combined_list)
