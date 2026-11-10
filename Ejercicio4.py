numero=(int(input("Introduce el numero: ")))
centenas = numero // 100
residuo = numero % 100
decenas = residuo // 10
unidades = residuo % 10

suma_cifras = centenas + decenas + unidades

numero_invertido = (unidades * 100) + (decenas * 10) + centenas
print(f"Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades}")
print(f"Suma de las cifras: {suma_cifras}")
print(f"Número invertido: {numero_invertido}")