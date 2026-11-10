#EJERCICIO 2
#Escribe un programa que pida una temperatura en grados Celsius y la muestre convertida a grados Fahrenheit y a Kelvin.
#Juan Agea Rodríguez
#10/11/2026
celsius=float(input("Introduce la temperatura en ºC: "))
F = celsius * 9/5 + 32
K = celsius + 273.15
print(celsius, "son", F, " F")
print (celsius, "son", K, " K")