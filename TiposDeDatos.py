#Tipos de datos

x=10 # int
y= 'Hola Mundo' # string
print(x)
print(y)

# Si queremos saber el tipo al que apunta esta variable se usa "type"
print(type(x))
print(type(y))


# agregar pista de a que tipo de dato apunta a una variable

z:str = 'Hola Mundo'

# solo es una indicacion, no quiere decir que solo almacene referencias de tipo string o int
                    # las variables de python son dinamicas
w:int = 'Hola Mundo'

#boleanos

X= True # tenemos que respetar mayusculas y minisculas en una literal
Y= False
print(X)
print(Y)
print(type(X))
print(type(Y))