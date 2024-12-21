List = [1, 2, 3, 4, 5, 6]
long = len(List)

while True:
    index = input("Veuillez entrer un index (ou -1 pour quitter): ")

    if not index.isdigit() and index != "-1":
        print("Veuillez entrer un index de type entier ou -1 pour quitter !")
        continue

    index = int(index)
    if index == -1:
        print("Fin !")
        break
    elif index < 0 or index >= long:
        print(f"Veuillez entrer un index entre 0 et {long - 1} (ou -1 pour quitter)  ")
    else:
        value = int(input("Veuillez entrer une valeur : "))
        List[index] = value
        print(List)
