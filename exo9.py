i = int(input("Enter the number of cities that you want to order: "))
j = 0
cities = []
while j < i:
    city = input(f"Enter the city number {j + 1}: ")
    long = len(city) 
    population = long * 1000000 
    cities.append((city, population))
    print(f"The city {city} has {long} letters, so its population is {population}.")
    j += 1  

cities.sort(key=lambda x: x[1], reverse=True)#on prend tout l'elemnt du tableau et on retourne la population

# Afficher les résultats triés
print("\nCities sorted by population:")
for city, population in cities:
    print(f"{city}: {population}")