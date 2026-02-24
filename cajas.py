# Área de 3x2
ancho = 3
alto = 2
area = [[0, 0], [0, 0], [0, 0]] # Representación simple

def lanzar_caja(x, y):
    area[x][y] += 1
    # Comprobar si todo el nivel está lleno (todos > 0)
    esta_lleno = True
    for fila in area:
        for celda in fila:
            if celda == 0: esta_lleno = False
            
    if esta_lleno:
        print("¡Nivel completo! Desaparece una capa.")
        for i in range(len(area)):
            for j in range(len(area[i])):
                area[i][j] -= 1

# Para consultar altura máxima
# max_h = max(max(fila) for fila in area)