print("Please enter informations below:")
total_achat=int(input("Total amount:"))
nb_items=int(input("Number of items:"))
day=input("Day of the week")
if day == "Saturday" or day == "Sunday":
    reduction=total_achat*20/100
else:
    reduction=total_achat*10/100

total_achat=total_achat-reduction

if nb_items>5:
        reduction_1=total_achat*5/100
        total_achat=total_achat-reduction_1

print(f"Total price after discount:{total_achat}")


