# Estructura inicial del personaje
personaje = {
    "nombre": "Jorge el Valiente",
    "clase": "Guerrero",
    "nivel": 1,
    "atributos": {
        "fuerza": 18,
        "porcentaje_fuerza": 50,  # El famoso 18/50
        "destreza": 12,
        "constitucion": 15,
        "inteligencia": 10,
        "sabiduria": 8,
        "carisma": 14
    },
    "vida_maxima": 10,
    "gaco": 20
}

print(f"Personaje: {personaje['nombre']} - Clase: {personaje['clase']}")

# Tabla de bonificadores de Fuerza (Simplificada para probar)
# Estructura: valor: (ajuste_ataque, ajuste_daño)
tabla_fuerza = {
    17: (1, 1),
    18: (1, 2)
}

valor_fuerza = personaje["atributos"]["fuerza"]
bonos = tabla_fuerza.get(valor_fuerza)

print(f"Con Fuerza {valor_fuerza}, tenés +{bonos[0]} al ataque y +{bonos[1]} al daño.")