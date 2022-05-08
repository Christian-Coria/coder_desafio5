def pares_impares(lista):
    #creamos las dos variables de listas vacias
    pares = [] 
    impares = []
    # iniciamosBucle for para iterar la lista.
    for i in lista:
        if i%2 == 0:
            # si es divisible por dos, es par y se añade a la lista pares
            pares.append(i)
        else:
            # si no es divisible por dos, es par y se añade a la lista pares
            impares.append(i)
    # Ordenamos las listas con .sort().
    pares.sort()
    impares.sort()
    # retornamos las listas de pares e impares.
    return pares, impares

lista = [3,2,1,7,8,9,4,6,5]
pares, impares = pares_impares(lista)
print("pares: ", pares )
print("impares: ", impares)




