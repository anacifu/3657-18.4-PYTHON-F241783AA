import time  # Importamos esto para que el ascensor no "teletransporte"

# Configuración inicial
piso_actual = 0
PISO_MIN = -2
PISO_MAX = 10

print("SISTEMA DE CONTROL DE ASCENSOR")
print(f"Pisos operativos: {PISO_MIN} hasta {PISO_MAX}")

# 1. Pedir el destino al usuario
try:
    destino = int(input(f"Estás en el piso {piso_actual}. ¿A qué piso quieres ir? "))

    # 2. Validar si el piso existe (Creatividad: usamos constantes)
    if destino < PISO_MIN or destino > PISO_MAX:
        print(f"Error: El piso {destino} está fuera de servicio.")
    elif destino == piso_actual:
        print("Ya te encuentras en este piso.")
    else:
        # 3. Movimiento del ascensor
        print("\nCerrando puertas... 🚪")
        
        while piso_actual != destino:
            if piso_actual < destino:
                piso_actual += 1
                movimiento = "Subiendo ⬆️"
            else:
                piso_actual -= 1
                movimiento = "Bajando ⬇️"
            
            # Simulamos el tiempo que tarda entre pisos
            time.sleep(0.5) 
            print(f"{movimiento} ... Planta {piso_actual}")

        print("\n¡Ding! Has llegado a tu destino. Que tenga/n un buen día.")

except ValueError:
    print("Error: Por favor, introduce un número válido.")