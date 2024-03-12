N = int(input("Ingrese la cantidad de numeros primos a generar: "))

print(f"Los núemros primos hasta {N} son:")
contador = 0
for i in range(0,N):
    divisor = 0
    for j in range(1, i+1):
        if i % i == 0:
            divisor = divisor + 1

    if divisor == 2:
        print(f"El número {i} es primo")
        contador = contador + 1
        
if contador == 0:
    print("No se encontraron números primos en el rango seleccionado.")
    

    
    