# Tabla de bonificadores de Fuerza 
# Estructura: valor: (ajuste_ataque, ajuste_daño)
def calcular_bonos_fuerza(valor, clase, porcentaje=0):
    # Valores Bajos
    if valor <= 3:
        return {"golpe": -3, "ajuste_daño": -1, "desc": "Paupérrima"}
    elif 4 <= valor <= 5:
        return {"golpe": -2, "ajuste_daño": -1, "desc": "Muy Débil"}
    elif 6 <= valor <= 7:
        return {"golpe": -1, "ajuste_daño": 0, "desc": "Muy Débil"}
    elif 8 <= valor <= 9:
        return {"golpe": 0, "ajuste_daño": 0, "desc": "Muy Débil"}
    elif 10 <= valor <= 11:
        return {"golpe": 0, "ajuste_daño": 0, "desc": "Muy Débil"}
    elif 12 <= valor <= 13:
        return {"golpe": 0, "ajuste_daño": 0, "desc": "Muy Débil"}
    elif 14 <= valor <= 15:
        return {"golpe": 0, "ajuste_daño": 0, "desc": "Muy Débil"}
    elif valor == 16:
        return {"golpe": 0, "ajuste_daño": +1, "desc": "Muy Débil"}
    elif valor == 17:
        return {"golpe": +1, "ajuste_daño": +1, "desc": "Muy Débil"}
    elif valor == 18:
        if clase.lower() != "guerrero":
            return {"golpe": +1, "ajuste_daño": +2, "desc": "18 Normal"}
        
        if 1 <= porcentaje <= 50:
            return {"golpe": +1, "ajuste_daño": +3, "desc": "18/01-50"}
        elif 51 <= porcentaje <= 75:
            return {"golpe": +2, "ajuste_daño": +3, "desc": "18/51-75"}
        elif 76 <= porcentaje <= 90:
            return {"golpe": +2, "ajuste_daño": +4, "desc": "18/76-90"}
        elif 91 <= porcentaje <= 99:
            return {"golpe": +2, "ajuste_daño": +5, "desc": "18/91-99"}
        elif porcentaje == 100:
            return {"golpe": +3, "ajuste_daño": +6, "desc": "18/00 (¡Bestial!)"}
    
    return {"golpe": 0, "ajuste_daño": 0, "desc": "Fuerza estándar"}

def calcular_bonos_destreza(valor):
    # Tabla simplificada de AD&D 2.5
    if valor <= 2:
        return {"reaccion": -5, "proyectil": -5, "defensa": 5}
    elif 3 <= valor <= 5:
        return {"reaccion": -3, "proyectil": -3, "defensa": 3}
    elif 6 <= valor <= 14:
        return {"reaccion": 0, "proyectil": 0, "defensa": 0}
    elif valor == 15:
        return {"reaccion": 0, "proyectil": 0, "defensa": -1}
    elif valor == 16:
        return {"reaccion": 1, "proyectil": 1, "defensa": -2}
    elif valor == 17:
        return {"reaccion": 2, "proyectil": 2, "defensa": -3}
    elif valor == 18:
        return {"reaccion": 3, "proyectil": 3, "defensa": -4}
    
    return {"reaccion": 0, "proyectil": 0, "defensa": 0}

def calcular_bonos_constitucion(valor, clase):
    # Tabla de Ajuste de Puntos de Golpe (PG)
    if valor <= 3:
        ajuste_pg = -2
    elif 4 <= valor <= 6:
        ajuste_pg = -1
    elif 7 <= valor <= 14:
        ajuste_pg = 0
    elif valor == 15:
        ajuste_pg = 1
    elif valor == 16:
        ajuste_pg = 2
        # Aquí empieza la diferencia para los Luchadores
    elif valor == 17:
        ajuste_pg = 3 if clase.lower() == "guerrero" else 2
    elif valor >= 18:
        ajuste_pg = 4 if clase.lower() == "guerrero" else 2
    else:
        ajuste_pg = 0
        
    return {"ajuste_pg": ajuste_pg}

# 1. Pedir el Nombre
nombre_pj = input("¿Cual es el nombre de tu heroe? ")

# 2. Pedir la clase
clase_pj = input("¿Cual es la clase de tu personaje? (Guerrero, Mago, etc.): ")

# 3.0 Pedir la fuerza
fuerza_pj = int(input("¿Que fuerza tiene? (3-18): "))

# Se aplica la logica de la clases luchador:
porcentaje_pj = 0
# Solo si es Guerrero (Luchador) Y tiene 18, pedimos porcentaje
if fuerza_pj == 18 and clase_pj.lower() == "guerrero":
    porcentaje_pj = int(input("¡Fuerza excepcional de Luchador! Poné el porcentaje (1-100): "))
    
# 3.1 Pedir la destreza
destreza_pj = int(input("¿Que destreza tiene? (3-18): "))

# 3.2 Pedir la constitucion
constitucion_pj = int(input("¿Que constitucion tiene? (3-18): "))

# 4. Cálculo de los bonos
bonos = calcular_bonos_fuerza(fuerza_pj, clase_pj, porcentaje_pj)
bonos_des = calcular_bonos_destreza(destreza_pj)
bonos_con = calcular_bonos_constitucion(constitucion_pj, clase_pj)

# Preparamos el texto de la fuerza (si es 18 y guerrero, sumamos el porcentaje)
if fuerza_pj == 18 and clase_pj.lower() == "guerrero":
    fuerza_texto = f"{fuerza_pj}/{'00' if porcentaje_pj == 100 else porcentaje_pj}"
else:
    fuerza_texto = f"{fuerza_pj}"

# LA LÍNEA MÁGICA (Todo en un solo renglón)
print("\n" + "="*55)
print(f" FICHA DE PERSONAJE: {nombre_pj.upper()} ")
print("="*55)
print(f"CLASE: {clase_pj.capitalize()}")
print(f"{'ATRIBUTO':<10} | {'VALOR':<10}")
print("-" * 55)
print(f"FUE: {fuerza_texto:<7} Probab. golpe: {bonos['golpe']}   Ajuste daño: {bonos['ajuste_daño']}")
print(f"DES: {destreza_pj:<7} Ajuste reacción: {bonos_des['reaccion']:>2}   Ajuste ataque proyect.: {bonos_des['proyectil']:>2}   Ajuste defensivo: {bonos_des['defensa']:>2}")
print(f"CON: {constitucion_pj:<7} Ajuste punto golpe: {bonos_con['ajuste_pg']:>2}")
print("="*55)