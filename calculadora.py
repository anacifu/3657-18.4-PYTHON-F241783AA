print("--- CALCULADORA DINÁMICA ---")

# 1. Empezamos con el primer número
resultado = float(input("Introduce el primer número: "))

while True:
    print(f"\nValor actual: {resultado}")
    operacion = input("Introduce símbolo (+, -, *, /) o pulsa ENTER para finalizar: ")

    # Si el usuario pulsa ENTER (vacío), salimos del bucle
    if operacion == "":
        break

    # Comprobamos que el símbolo sea válido
    if operacion not in ['+', '-', '*', '/']:
        print("Símbolo no válido. Usa +, -, * o /")
        continue

    # 2. Pedimos el siguiente número para la operación
    try:
        siguiente_numero = float(input("Introduce la siguiente cantidad: "))
        
        # 3. Aplicamos la operación al acumulador
        if operacion == '+':
            resultado += siguiente_numero
        elif operacion == '-':
            resultado -= siguiente_numero
        elif operacion == '*':
            resultado *= siguiente_numero
        elif operacion == '/':
            if siguiente_numero != 0:
                resultado /= siguiente_numero
            else:
                print("¡Error! No se puede dividir por cero.")
    except ValueError:
        print("Error: Introduce un número válido.")

print(f"\n--- RESULTADO FINAL: {resultado} ---")
print("¡Gracias por usar la calculadora!")