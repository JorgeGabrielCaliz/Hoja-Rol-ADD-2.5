import os

# Tabla de modificadores raciales
TABLA_RAZAS = {
    "humano": {"FUE": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0},
    "Semielfo": {"FUE": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0},
    "elfo":   {"FUE": 0, "DES": 1, "CON": -1, "INT": 0, "SAB": 0, "CAR": 0},
    "enano":  {"FUE": 0, "DES": 0, "CON": 1, "INT": 0, "SAB": 0, "CAR": -1},
    "gnomo":  {"FUE": 0, "DES": 0, "CON": 0, "INT": 1, "SAB": -1, "CAR": 0}, # Depende de la subraza, pero usemos esta
    "halfling": {"FUE": -1, "DES": 1, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0}
}
# Tabla de bonificadores de Fuerza
def calcular_bonos_fuerza(valor, clase, porcentaje=0):
    # Formato: (golpe, daño, peso_perm, esfuerzo_max, abrir_puertas, barras_rejas, nota)
    tablas = {
        1:  (-5, -4, 1, 3, "1", 0, ""),
        2:  (-3, -2, 2, 5, "1", 0, ""),
        3:  (-3, -1, 5, 10, "2", 0, ""),
        4:  (-2, -1, 10, 25, "3", 0, ""),
        5:  (-2, -1, 10, 25, "3", 0, ""),
        6:  (-1, 0, 20, 55, "4", 0, ""),
        7:  (-1, 0, 20, 55, "4", 0, ""),
        8:  (0, 0, 35, 90, "5", 1, ""),
        9:  (0, 0, 35, 90, "5", 1, ""),
        10: (0, 0, 40, 115, "6", 2, ""),
        11: (0, 0, 40, 115, "6", 2, ""),
        12: (0, 0, 45, 140, "7", 4, ""),
        13: (0, 0, 45, 140, "7", 4, ""),
        14: (0, 0, 55, 170, "8", 7, ""),
        15: (0, 0, 55, 170, "8", 7, ""),
        16: (0, 1, 70, 195, "9", 10, ""),
        17: (1, 1, 85, 220, "10", 13, ""),
        18: (1, 2, 110, 280, "11", 16, ""),
        # Fuerza Excepcional (Luchadores) 
        "18/50": (1, 3, 135, 380, "12", 20, "Excepcional"),
        "18/75": (2, 3, 160, 530, "13", 25, "Excepcional"),
        "18/90": (2, 4, 185, 640, "14", 30, "Excepcional"),
        "18/99": (2, 5, 235, 750, "15(3)", 35, "Excepcional"),
        "18/00": (3, 6, 335, 1000, "16(6)", 40, "Bestial"), # El famoso 18/00
        # Fuerzas de Gigante (19+)
        19: (3, 7, 485, 1500, "16(8)", 50, "Gigante Colinas"), # Gigante de las Colinas 
        20: (3, 8, 535, 2000, "17(10)", 60, "Gigante Piedra"), # Gigante de Piedra 
        21: (4, 9, 635, 2500, "17(12)", 70, "Gigante Escarchas"), # Gigante de las Escarchas 
        22: (4, 10, 785, 3000, "18(14)", 80, "Gigante Fuego"), # Gigante de Fuego 
        23: (5, 11, 935, 4000, "18(16)", 90, "Gigante Nubes"), # Gigante de las Nubes 
        24: (6, 12, 1235, 5000, "19(17)", 95, "Gigante Tormentas"), # Gigante de las Tormentas 
        25: (7, 14, 1535, 7500, "19(18)", 99, "Titán") # Titán 
    }

    clave = valor
    if valor == 18 and clase.lower() == "guerrero":
        if 1 <= porcentaje <= 50:
            clave = "18/50"
        elif 51 <= porcentaje <= 75:
            clave = "18/75"
        elif 76 <= porcentaje <= 90:
            clave = "18/90"
        elif 91 <= porcentaje <= 99:
            clave = "18/99"
        elif porcentaje == 100:
            clave = "18/00"

    res = tablas.get(clave, (0, 0, 40, 115, "6", 2, ""))

    return {
        "golpe": res[0],
        "ajuste_daño": res[1],
        "peso_perm": res[2],
        "esfuerzo_max": res[3],
        "abrir_puertas": res[4],
        "barras_rejas": res[5],
        "nota": res[6]
    }

def calcular_bonos_destreza(valor):
    # Tabla simplificada de AD&D 2.5
    if valor <= 2:
        return {"reaccion": -5, "proyectil": -5, "defensa": 5}
    elif 3 <= valor <= 6:
        return {"reaccion": -3, "proyectil": -3, "defensa": 3}
    elif 7 <= valor <= 14:
        return {"reaccion": 0, "proyectil": 0, "defensa": 0}
    elif valor == 15:
        return {"reaccion": 0, "proyectil": 0, "defensa": -1}
    elif valor == 16:
        return {"reaccion": 1, "proyectil": 1, "defensa": -2}
    elif valor == 17:
        return {"reaccion": 2, "proyectil": 2, "defensa": -3}
    elif valor == 18:
        return {"reaccion": 2, "proyectil": 2, "defensa": -4}
    elif valor == 19:
        return {"reaccion": 3, "proyectil": 3, "defensa": -4}
    elif valor == 20:
        return {"reaccion": 3, "proyectil": 3, "defensa": -4}
    elif valor == 21:
        return {"reaccion": 4, "proyectil": 4, "defensa": -5}
    
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

def calcular_bonos_inteligencia(valor):
    # El idioma natal siempre se sabe (1)
    # A partir de 9 empiezan los adicionales
    if valor <= 8:
        lenguajes = 1 # Solo el natal
    elif 9 <= valor <= 11:
        lenguajes = 2 # Natal + 1 adicional
    elif 12 <= valor <= 13:
        lenguajes = 3 # Natal + 2 adicionales
    elif 14 <= valor <= 15:
        lenguajes = 4 # Natal + 3 adicionales
    elif valor == 16:
        lenguajes = 5 # Natal + 4 adicionales
    elif valor == 17:
        lenguajes = 6 # Natal + 5 adicionales
    elif valor == 18:
        lenguajes = 7 # Natal + 6 adicionales
    else:
        lenguajes = 1
    return {"lenguajes": lenguajes}

def calcular_bonos_sabiduria(valor):
    # Ajuste de defensa contra magia mental
    if valor <= 2:
        defensa_mental = -4
    elif valor == 3:
        defensa_mental = -3
    elif valor == 4:
        defensa_mental = -2
    elif 5 <= valor <= 7:
        defensa_mental = -1
    elif 8 <= valor <= 14:
        defensa_mental = 0
    elif valor == 15:
        defensa_mental = 1
    elif valor == 16:
        defensa_mental = 2
    elif valor == 17:
        defensa_mental = 3
    elif valor == 18:
        defensa_mental = 4
    else:
        defensa_mental = 0
    return {"def_mental": defensa_mental}

def calcular_bonos_carisma(valor):
    if valor <= 2:
        return {"seguidores": 1, "lealtad": -7, "reaccion": -6}
    elif valor == 3:
        return {"seguidores": 1, "lealtad": -6, "reaccion": -5}
    elif 4 <= valor <= 5:
        return {"seguidores": 2, "lealtad": -4, "reaccion": -3}
    elif 6 <= valor <= 8:
        return {"seguidores": 3, "lealtad": -2, "reaccion": -1}
    elif 9 <= valor <= 12:
        return {"seguidores": 4, "lealtad": 0, "reaccion": 0}
    elif valor == 13:
        return {"seguidores": 5, "lealtad": 0, "reaccion": 1}
    elif valor == 14:
        return {"seguidores": 6, "lealtad": 1, "reaccion": 2}
    elif valor == 15:
        return {"seguidores": 7, "lealtad": 3, "reaccion": 3}
    elif valor == 16:
        return {"seguidores": 8, "lealtad": 4, "reaccion": 5}
    elif valor == 17:
        return {"seguidores": 10, "lealtad": 6, "reaccion": 6}
    elif valor == 18:
        return {"seguidores": 15, "lealtad": 8, "reaccion": 7}
    
    return {"seguidores": 0, "lealtad": 0, "reaccion": 0}

# 1. Datos básicos
nombre_pj = input("¿Cual es el nombre de tu heroe? ")
raza_pj = input("¿Cual es tu raza? (Humano, Elfo, Semielfo, Enano, Gnomo, Halfling): ").lower()
clase_pj = input("¿Cual es tu clase? (Guerrero, Mago, etc.): ")

# 2. Pedir Atributos "Base" (lo que salió en los dados)
fuerza_base = int(input("Fuerza base (3-18): "))
destreza_base = int(input("Destreza base (3-18): "))
constitucion_base = int(input("Constitucion base (3-18): "))
inteligencia_base = int(input("Inteligencia base (3-18): "))
sabiduria_base = int(input("Sabiduria base (3-18): "))
carisma_base = int(input("Carisma base (3-18): "))

  
# 3. APLICAR MODIFICADORES RACIALES
# Buscamos los bonos de la raza elegida (si no existe, usamos 0)
bonos_raza = TABLA_RAZAS.get(raza_pj, {"FUE": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0})

fuerza_pj = fuerza_base + bonos_raza.get("FUE", 0)
destreza_pj = destreza_base + bonos_raza.get("DES", 0)
constitucion_pj = constitucion_base + bonos_raza.get("CON", 0)
inteligencia_pj = inteligencia_base + bonos_raza.get("INT", 0)
sabiduria_pj = sabiduria_base + bonos_raza.get("SAB", 0)
carisma_pj = carisma_base + bonos_raza.get("CAR", 0)


# 3.1 Se aplica la logica de la clases luchador:
porcentaje_pj = 0
# Solo si es Guerrero (Luchador) Y tiene 18, pedimos porcentaje
if fuerza_pj == 18 and clase_pj.lower() == "guerrero":
    porcentaje_pj = int(input("¡Fuerza excepcional de Luchador! Poné el porcentaje (1-100): "))


# 4. Cálculo de los bonos
bonos_fue = calcular_bonos_fuerza(fuerza_pj, clase_pj, porcentaje_pj)
bonos_des = calcular_bonos_destreza(destreza_pj)
bonos_con = calcular_bonos_constitucion(constitucion_pj, clase_pj)
bonos_int = calcular_bonos_inteligencia(inteligencia_pj)
bonos_sab = calcular_bonos_sabiduria(sabiduria_pj)
bonos_car = calcular_bonos_carisma(carisma_pj)


# Preparamos el texto de la fuerza (si es 18 y guerrero, sumamos el porcentaje)
if fuerza_pj == 18 and clase_pj.lower() == "guerrero":
    fuerza_texto = f"{fuerza_pj}/{'00' if porcentaje_pj == 100 else porcentaje_pj}"
else:
    fuerza_texto = f"{fuerza_pj}"

# Esto limpia la pantalla según el sistema operativo
os.system('cls' if os.name == 'nt' else 'clear')
# LA LÍNEA MÁGICA DE LA HOJA
print("\n" + "="*55)
print(f" FICHA DE PERSONAJE: {nombre_pj.upper()} ")
print("="*55)
print(f"CLASE: {clase_pj.capitalize()} RAZA: {raza_pj.capitalize()}")
print(f"{'ATRIBUTO':<10} | {'VALOR':<10}")
print("-" * 55)
print(f"FUE: {fuerza_pj:<2} ({porcentaje_pj if porcentaje_pj > 0 else '--':>2}) | Golpe: {bonos_fue['golpe']:>2} | Daño: {bonos_fue['ajuste_daño']:>2} | Carga: {bonos_fue['peso_perm']:>3}/{bonos_fue['esfuerzo_max']:>4} | Puertas: {bonos_fue['abrir_puertas']:>5} | Barras: {bonos_fue['barras_rejas']:>2}%")
if bonos_fue['nota']:
    print(f"      [ NOTA: {bonos_fue['nota']} ]")
print(f"DES: {destreza_pj:<7} Ajuste reacción: {bonos_des['reaccion']:>2}   Ajuste ataque proyect.: {bonos_des['proyectil']:>2}   Ajuste defensivo: {bonos_des['defensa']:>2}")
print(f"CON: {constitucion_pj:<7} Ajuste punto golpe: {bonos_con['ajuste_pg']:>2}")
print(f"INT: {inteligencia_pj:<7} Núm. de lenguajes: {bonos_int['lenguajes']:>2}")
print(f"SAB: {sabiduria_pj:<7} Ajuste defensa magica: {bonos_sab['def_mental']:>2}")
print(f"CAR: {carisma_pj:<7} Núm. máx. servidores: {bonos_car['seguidores']:>2}   Lealtad básica: {bonos_car['lealtad']:>2}   Ajuste de reacción: {bonos_car['reaccion']:>2}")
print("="*55)
if bonos_fue['nota']:
    print(f"NOTAS DE FUERZA: {bonos_fue['nota']}")

print(f"CARGA: {bonos_fue['peso_perm']} lbs (Máx: {bonos_fue['esfuerzo_max']})")
print(f"ACCIONES: Abrir Puertas: {bonos_fue['abrir_puertas']}/20 | Barras/Rejas: {bonos_fue['barras_rejas']}%")
print("=" * 55)