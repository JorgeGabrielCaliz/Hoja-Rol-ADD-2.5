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
def calcular_bonos_fuerza(valor, porcentaje=0):
    # Primero chequeamos si es fuerza 18
    if valor == 18:
        if porcentaje == 0:
            return {"ataque": 1, "daño": 2, "desc": "18 normal"}
        elif 1 <= porcentaje <= 50:
            return {"ataque": 1, "daño": 3, "desc": "18/01-50"}
        elif 51 <= porcentaje <= 75:
            return {"ataque": 2, "daño": 3, "desc": "18/51-75"}
        elif 76 <= porcentaje <= 90:
            return {"ataque": 2, "daño": 4, "desc": "18/76-90"}
        elif 91 <= porcentaje <= 99:
            return {"ataque": 2, "daño": 5, "desc": "18/91-99"}
        elif porcentaje == 100:
            return {"ataque": 3, "daño": 6, "desc": "18/00 (¡Bestial!)"}
    
    return {"ataque": 0, "daño": 0, "desc": "Fuerza estándar"}

# Hagamos una prueba rápida:
mi_fuerza = 18
mi_porcentaje = 100 # Probemos el 18/00

resultado = calcular_bonos_fuerza(mi_fuerza, mi_porcentaje)

print(f"Resultado para {resultado['desc']}:")
print(f"Bono al ataque: +{resultado['ataque']}")
print(f"Bono al daño: +{resultado['daño']}")