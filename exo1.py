name=input("Please enter u'r name :")
if name=="VIP":
    print("Enjoy the show for free!")
else:
    nb_tickets=int(input("How many tickets would you like to buy?"))
    total_cost=nb_tickets*15.50
    print(f"The total cost is {total_cost}")
    print("Enjoy your tickets!")