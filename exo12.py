width = int(input("Veuillez entrer la largeur d'un bloc : "))
height = int(input("Veuillez entrer la hauteur totale : "))

j = 0
while j < height:
    print("#" * width, end=" ")
    j += 1
