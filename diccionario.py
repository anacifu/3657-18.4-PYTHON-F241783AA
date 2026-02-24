# Primero pedimos los datos
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Creamos el diccionario ya con los datos (como pidió Joaquín)
persona = {
    "nombre": nombre,
    "edad": edad
}

# Aplicamos la lógica de censura
if persona["edad"] < 18:
    persona["nombre"] = "###"
    print(f"USUARIO MENOR DE EDAD: {persona}")
else:
    print(f"USUARIO AUTORIZADO: {persona}")