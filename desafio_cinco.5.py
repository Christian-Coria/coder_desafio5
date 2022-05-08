#definimos la funcion y le pasamos 3 parametros

def recortar(num_rec, num_min, num_max):
    #definimos las condicionales en un bloque if/elif
    if num_rec < num_min:
         return num_min
    elif num_rec > num_max:
        return num_max
    return num_rec

print(recortar(15, 0, 10))   
print(recortar(50, 10, 80))   
print(recortar(0, 90, 10))   
        
