animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
temp_list = list(animal_movies)
temp_list.append("Dumbo")
temp_list.append("Zootopia")
animal_movies = tuple(temp_list)
del temp_list

print("Updated animal movies:", animal_movies)