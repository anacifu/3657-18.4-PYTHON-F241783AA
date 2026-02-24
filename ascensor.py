piso_actual = 0
print("--- BIENVENIDO AL ASCENSOR TAJAMAR ---")
print("Pisos disponibles: del -2 (Sótano) al 10 (Ático)")

destino = int(input("¿A qué piso deseas subir/bajar?: "))

if destino < -2 or destino > 10:
    print(f"Error: El piso {destino} no existe en este edificio.")
else:
    print(f"Saliendo del piso {piso_actual}...")
    
    # Bucle para mover el ascensor paso a paso
    while piso_actual != destino:
        if piso_actual < destino:
            piso_actual += 1
        else:
            piso_actual -= 1
        print(f"Elevador en planta: {piso_actual}...")

    print(f"¡Ding! Has llegado al piso {piso_actual}. Ten un buen día.")