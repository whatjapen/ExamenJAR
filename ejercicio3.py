#EJERCICIO 3
#Un servidor guarda el tiempo que lleva encendido como una cantidad total de segundos. Escribe un programa que pida esa cantidad (número entero) y muestre a cuántos días, horas, minutos y segundos corresponde.
#Juan Agea Rodríguez
#10/11/2026
segundos_totales = int(input("Introduce el tiempo en segundos: "))

SEGUNDOS_MINUTO = 60
SEGUNDOS_HORA = 3600
SEGUNDOS_DIA = 86400

dias = segundos_totales // SEGUNDOS_DIA
segundos_restantes = segundos_totales % SEGUNDOS_DIA

horas = segundos_restantes // SEGUNDOS_HORA
segundos_restantes = segundos_restantes % SEGUNDOS_HORA

minutos = segundos_restantes // SEGUNDOS_MINUTO
segundos = segundos_restantes % SEGUNDOS_MINUTO
print(f"{segundos_totales} segundos son {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")