nb_personnes=int(input("How many people need a ride?"))
nb_pers_taxi=int(input("How many people fit in one taxi?"))
nb_taxi_pleins=nb_personnes //nb_pers_taxi

if nb_personnes % nb_pers_taxi==0 :
    nb_taxi_pleins=nb_personnes //nb_pers_taxi
else:
    nb_taxi_pleins=nb_taxi_pleins+1
  
  
print(f"Number of taxis needed: { nb_taxi_pleins}")
 