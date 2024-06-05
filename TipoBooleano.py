# Tipo Booleano
# Nos permite saber si un valor es True o False

miVariable = False
print(miVariable)

miVariable = 3 > 2 # deberia devolver verdadero
print(miVariable)

miVariable = 1 > 2
print(miVariable)

if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")
# Tira como resultado falso, porque 1 no es mayor que 2

miVariable = 1 < 2

if miVariable:
    print('El resultado fue verdadero')
else:
    print('El resultado fue falso')
# Tira como resultado verdadero, porque 1 es menor que 2


