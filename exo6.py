import math
price=float(input("Please type in a price:"))
centimes,Dinars  = math.modf(price)
dinars = int(price)  # Partie entière
centimes = round((price - dinars) * 100)  # Partie fractionnaire

print(f"Dinars:{dinars }")
print(f"Centimes:{centimes}")