n1 = input("Ingresa el primer numero")
n2 = input("Ingresa el segundo numero")

n1=int(n1)
n2=int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
divicion = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
El resultado de la suma es {suma}
El resultado de la resta es {resta}
El resultado de la multiplicacion es {multiplicacion}
El resultado de la divcion es {divicion}
"""

print(mensaje)
