#importamos el modulo math para obtener el valor de pi
import math
#Calcula el área de un círculo de 5 de radio
 
#creamos la funcion con las variables de pi para su respectivo valor
#  y area (para introducir su formula matematica)
# imprimimos el resultado del calculo de laa funcion indicando que solo imprima 2 digitos despues de la coma
def area_circulo(radio):
    pi = math.pi
    area = (radio**2) * pi
    print(f"El area del Circulo es {area:.2f}")
# llamamos a la funcion y pasamos el argumento del radio para el calculo (5 segun consigna)
area_circulo(5)

