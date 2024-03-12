# es numero primo:
numero = int(input("Ingrese un número: "))

divisor = 0
for i in range(1, numero+1):
    if numero % i == 0:
        divisor = divisor + 1

if divisor == 2:
    print(f"El número {numero} es primo")
else:
    print (f"El número {numero} no es primo")
    
