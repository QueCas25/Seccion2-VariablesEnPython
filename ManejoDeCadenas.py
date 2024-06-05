# Manejo de Cadenas

# Cadena (String)

# Vamos a concatenar cadenas
miGrupoFavorito = "Morat"
miGrupoFavorito2 = "Morat" + " La mejor banda de amor"
# o
miGrupoFavorito3 = "Morat" " " "La mejor banda de amor"
print(miGrupoFavorito)

# concatenacion: es unir una o mas cadenas
print("Mi grupo favorito es: " + miGrupoFavorito)
print("Mi grupo favorito es: " + miGrupoFavorito2)
print("Mi grupo favorito es: " + miGrupoFavorito3)


# Un error, queremos sumar pero se concatenan

numero1 = "1"
numero2 = "2"

print(numero1 + numero2)
# hay de dos
# convertir el string a tipo entero o usar una literal de tipo entero

# Usamos literales de tipo entero
Numero1 = 1
Numero2 = 2

print(Numero1 + Numero2)

# Convertir a entero
numeroUno = "1"
numeroDos = "2"

# Aqui concatenamos
print("Concatenacion: ", numeroUno + numeroDos)

# Aqui se convierte a entero
print("Suma: ", int(numeroUno) + int(numeroDos))
