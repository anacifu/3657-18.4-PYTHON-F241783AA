estudiantes = [
    {"nombre": "Paula", "edad": 24, "notas": [7.5, 5.1, 3.0, 7.7]},
    {"nombre": "David", "edad": 666, "notas": [3.3, 6.2, 7.8, 4.9]},
    {"nombre": "Carlos", "edad": 6, "notas": [3.0, 6.9, 7.8, 1.0]}
]

for estudiante in estudiantes:
    maxima = max(estudiante["notas"])
    minima = min(estudiante["notas"])
    media = sum(estudiante["notas"]) / len(estudiante["notas"])
    
    # Todo en una línea con f-string impecable
    print(f"Estudiante: {estudiante['nombre']} | Máxima: {maxima} | Mínima: {minima} | Media: {media:.2f}")