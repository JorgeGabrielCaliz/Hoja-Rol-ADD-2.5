import os

# --- TABLA DE LÍMITES RACIALES (Manual del Jugador 2.5) --- 
LIMITES_RACIALES = {
    "humano":   {"FUE": (3, 18), "DES": (3, 18), "CON": (3, 18), "INT": (3, 18), "SAB": (3, 18), "CAR": (3, 18)},
    "enano":    {"FUE": (8, 18), "DES": (3, 17), "CON": (11, 19), "INT": (3, 18), "SAB": (3, 18), "CAR": (3, 17)},
    "elfo":     {"FUE": (3, 18), "DES": (6, 19), "CON": (7, 18), "INT": (8, 18), "SAB": (3, 18), "CAR": (8, 18)},
    "gnomo":    {"FUE": (6, 18), "DES": (3, 18), "CON": (8, 18), "INT": (6, 18), "SAB": (3, 18), "CAR": (3, 18)},
    "semielfo": {"FUE": (3, 18), "DES": (6, 18), "CON": (6, 18), "INT": (4, 18), "SAB": (3, 18), "CAR": (3, 18)},
    "halfling": {"FUE": (7, 18), "DES": (7, 19), "CON": (10, 18), "INT": (6, 18), "SAB": (3, 17), "CAR": (3, 18)}
}
# Tabla de modificadores raciales 
TABLA_RAZAS = {
    "humano": {"FUE": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0},
    "semielfo": {"FUE": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0},
    "elfo":   {"FUE": 0, "DES": 1, "CON": -1, "INT": 0, "SAB": 0, "CAR": 0},
    "enano":  {"FUE": 0, "DES": 0, "CON": 1, "INT": 0, "SAB": 0, "CAR": -1},
    "gnomo":  {"FUE": 0, "DES": 0, "CON": 0, "INT": 1, "SAB": -1, "CAR": 0},
    "halfling": {"FUE": -1, "DES": 1, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0}
}

# --- FUNCIÓN DE VALIDACIÓN ---
def validar_y_avisar(atributo, valor, raza, habilitado, soltura):
    if not habilitado: return
    limites = LIMITES_RACIALES.get(raza, {}).get(atributo)
    if limites:
        minimo, maximo = limites
        if valor < minimo or valor > maximo:
            print(f"\n⚠️  [AVISO]: {atributo} {valor} está fuera del rango legal para {raza.capitalize()} ({minimo}-{maximo}).")
            if soltura:
                print(">>> Permitido por ajuste de ambientación.")
            else:
                print(">>> ATENCIÓN: Este valor no es legal en reglas puras.")


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
    # Formato: (ajuste_rc, ajuste_proy, ajuste_def)
    tablas = {
        1: (-6, -6, +5),
        2: (-4, -4, +5),
        3: (-3, -3, +4),
        4: (-2, -2, +3),
        5: (-1, -1, +2),
        6: (0, 0, +1),
        7: (0, 0, 0),
        8: (0, 0, 0),
        9: (0, 0, 0),
        10: (0, 0, 0),
        11: (0, 0, 0),
        12: (0, 0, 0),
        13: (0, 0, 0),
        14: (0, 0, 0),
        15: (0, 0, -1),
        16: (+1, +1, -2),
        17: (+2, +2, -3),
        18: (+2, +2, -4),
        19: (+3, +3, -4),
        20: (+3, +3, -4),
        21: (+4, +4, -5),
        22: (+4, +4, -5),
        23: (+4, +4, -5),
        24: (+5, +5, -6),
        25: (+5, +5, -6)
    }
    
    res = tablas.get(valor, (0, 0, 0))
    return {
        "ajuste_rc": res[0],
        "ajuste_proy": res[1],
        "ajuste_def": res[2]
    }

def calcular_bonos_constitucion(valor, clase):
    # Formato: (ajuste_dg, supervivencia_shock, resurreccion, veneno, regeneracion)
    tablas = {
        1: (-3, 25, 30, -2, "Nulo"),
        2: (-2, 30, 35, -1, "Nulo"),
        3: (-2, 35, 40, 0, "Nulo"),
        4: (-1, 40, 45, 0, "Nulo"),
        5: (-1, 45, 50, 0, "Nulo"),
        6: (-1, 50, 55, 0, "Nulo"),
        7: (0, 55, 60, 0, "Nulo"),
        8: (0, 60, 65, 0, "Nulo"),
        9: (0, 65, 70, 0, "Nulo"),
        10: (0, 70, 75, 0, "Nulo"),
        11: (0, 75, 80, 0, "Nulo"),
        12: (0, 80, 85, 0, "Nulo"),
        13: (0, 85, 90, 0, "Nulo"),
        14: (0, 88, 92, 0, "Nulo"),
        15: (1, 90, 94, 0, "Nulo"),
        16: (2, 95, 96, 0, "Nulo"),
        17: (3, 97, 98, 0, "Nulo"),
        18: (4, 99, 100, 0, "Nulo"),
        19: (5, 99, 100, 1, "Nulo"),
        20: (5, 99, 100, 1, "1/6 turnos"),
        21: (6, 99, 100, 2, "1/5 turnos"),
        22: (6, 99, 100, 2, "1/4 turnos"),
        23: (6, 99, 100, 3, "1/3 turnos"),
        24: (7, 99, 100, 3, "1/2 turnos"),
        25: (7, 99, 100, 4, "1/1 turno")
    }
    
    res = tablas.get(valor, (0, 75, 80, 0, "Nulo"))
    
    ajuste_final = res[0]
    
    # Lista de clases que SI pueden tener más de +2
    clases_pro = ["guerrero", "paladin", "explorador", "ranger"]
    
    # Si la clase NO está en la lista y el ajuste es mayor a 2, se lo bajamos a 2
    if clase.lower() not in clases_pro and ajuste_final > 2:
        ajuste_final = 2

    return {
        "ajuste_dg": ajuste_final,
        "shock": res[1],
        "resurreccion": res[2],
        "veneno": res[3],
        "regen": res[4]
    }

def calcular_bonos_inteligencia(valor):
    # Formato: (lenguajes, nivel_max, prob_aprender, max_conjuros, inm_ilusion)
    tablas = {
        1:  (0, 0, 0, 0, "Ninguna"),
        2:  (1, 0, 0, 0, "Ninguna"),
        3:  (1, 0, 0, 0, "Ninguna"),
        4:  (1, 0, 0, 0, "Ninguna"),
        5:  (1, 0, 0, 0, "Ninguna"),
        6:  (1, 0, 0, 0, "Ninguna"),
        7:  (1, 0, 0, 0, "Ninguna"),
        8:  (1, 0, 0, 0, "Ninguna"),
        9:  (2, 4, 35, 6, "Ninguna"),
        10: (2, 5, 40, 7, "Ninguna"),
        11: (2, 5, 45, 7, "Ninguna"),
        12: (3, 6, 50, 7, "Ninguna"),
        13: (3, 6, 55, 9, "Ninguna"),
        14: (4, 7, 60, 9, "Ninguna"),
        15: (4, 7, 65, 11, "Ninguna"),
        16: (5, 8, 70, 11, "Ninguna"),
        17: (6, 8, 75, 14, "Ninguna"),
        18: (8, 9, 85, 18, "Ninguna"),
        19: (9, 9, 95, 99, "1er Nivel"),
        20: (10, 9, 96, 99, "2do Nivel"),
        21: (11, 9, 97, 99, "3er Nivel"),
        22: (12, 9, 98, 99, "4to Nivel"),
        23: (13, 9, 99, 99, "5to Nivel"),
        24: (14, 9, 100, 99, "6to Nivel"),
        25: (15, 9, 100, 99, "7mo Nivel")
    }
    res = tablas.get(valor, (1, 0, 0, 0, "Ninguna"))
    return {
        "lenguajes": res[0], 
        "nivel_max": res[1], 
        "prob_aprender": res[2], 
        "max_conjuros": res[3], 
        "inm_ilusion": res[4]
    }

def calcular_bonos_sabiduria(valor):
    # Formato: (ajuste_def, fracaso_conjuro, conjuros_bono, inm_mental)
    tablas = {
        # ... (del 1 al 12: fracaso progresivo) ...
        1: (-6, "-", 80, "-"),
        2: (-4, "-", 60, "-"),
        3: (-3, "-", 50, "-"),
        4: (-2, "-", 45, "-"),
        5: (-1, "-", 40, "-"),
        6: (-1, "-", 35, "-"),
        7: (-1, "-", 30, "-"),
        8: (0, "-", 25, "-"),
        9: (0, "0", 20, "-"),
        10: (0, "0", 15, "-"),
        11: (0, "0", 10, "-"),
        12: (0, "0", 5, "-"),
        13: (0, "1", 0, "Ninguna"),
        14: (0, "1", 0, "Ninguna"),
        15: (+1, "2", 0, "Ninguna"),
        16: (+2, "2", 0, "Ninguna"),
        17: (+3, "3", 0, "Ninguna"),
        18: (+4, "4", 0, "Ninguna"),
        # Sabiduría Divina (19+)
        19: (+4, "1,4", 0, "Causa miedo, Encantamiento de persona, Autoridad, Amigos, Hipnotismo"),
        20: (+4, "2,4", 0, "Olvidar, Retencion de personas, Rayo debilitador, Intimidacion"),
        21: (+4, "3,5", 0, "Miedo"),
        22: (+4, "4,5", 0, "Encantamiento de monstruo, Confusion, Emocion, Tanteo, Sugestion"),
        23: (+4, "5,5", 0, "Caos, Debilidad mental, Retencion de personalidad, Frasco magico, Busqueda"),
        24: (+4, "6,6", 0, "Geas, Sugestion de masas, Varita de liderazgo"),
        25: (+4, "6,7", 0, "Antipatia/simpatia, Conjuro de muerte, Encantamiento de masas")
    }
    # Nota: Las inmunidades mentales en 19+ son por hechizos específicos
    res = tablas.get(valor, (0, "0", 0, "Ninguna"))
    return {
        "defensa": res[0],
        "bonos": res[1],
        "fracaso": res[2],
        "inmunidad": res[3]
    }

def calcular_bonos_carisma(valor):
    # Formato: (max_seg, lealtad_bas, ajuste_rc)
    tablas = {
        1: (0, -8, -7),
        2: (1, -7, -6),
        3: (1, -6, -5),
        4: (1, -5, -4),
        5: (2, -4, -3),
        6: (2, -3, -2),
        7: (3, -2, -1),
        8: (3, 0, 0),
        9: (4, -0, 0),
        10: (4, -0, 0),
        11: (4, -0, 0),
        12: (5, -0, 0),
        13: (5, 0, 1),
        14: (6, 1, 2),
        15: (7, 3, 3),
        16: (8, 4, 5),
        17: (10, 6, 6),
        18: (15, 8, 7),
        19: (20, 10, 8),
        20: (25, 12, 9),
        21: (30, 14, 10),
        22: (35, 16, 11),
        23: (40, 18, 12),
        24: (45, 20, 13),
        25: (50, 22, 14)
    }
    res = tablas.get(valor, (0, 0, 0))
    return {
        "max_seg": res[0],
        "lealtad_bas": res[1],
        "ajuste_rc": res[2]
    }

# --- FLUJO PRINCIPAL ---

# 1. Datos básicos
nombre_pj = input("¿Cual es el nombre de tu heroe? ")
raza_pj = input("¿Cual es tu raza? (Humano, Elfo, Semielfo, Enano, Gnomo, Halfling): ").lower()

# --- INTERRUPTORES RAZAS ---
print("\n" + "="*40)
validar_topes = input("¿Validar límites de Atributos por Raza? (S/N): ").upper() == "S"
soltura_master = input("¿Modo Ambientación (solo avisar)? (S/N): ").upper() == "S"
print("="*40 + "\n")

clase_pj = input("¿Cual es tu clase? (Guerrero, Mago, etc.): ")

# 2. Pedir Atributos "Base"
fuerza_base = int(input("Fuerza base: "))
validar_y_avisar("FUE", fuerza_base, raza_pj, validar_topes, soltura_master)
destreza_base = int(input("Destreza base: "))
validar_y_avisar("DES", destreza_base, raza_pj, validar_topes, soltura_master)
constitucion_base = int(input("Constitucion base: "))
validar_y_avisar("CON", constitucion_base, raza_pj, validar_topes, soltura_master)
inteligencia_base = int(input("Inteligencia base: "))
validar_y_avisar("INT", inteligencia_base, raza_pj, validar_topes, soltura_master)
sabiduria_base = int(input("Sabiduria base: "))
validar_y_avisar("SAB", sabiduria_base, raza_pj, validar_topes, soltura_master)
carisma_base = int(input("Carisma base: "))
validar_y_avisar("CAR", carisma_base, raza_pj, validar_topes, soltura_master)

  
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
print(f"DES: {destreza_pj:<2} | Reacción: {bonos_des['ajuste_rc']:>2} | Proyectiles: {bonos_des['ajuste_proy']:>2} | Defensa: {bonos_des['ajuste_def']:>2}")
print(f"CON: {constitucion_pj:<2} | Ajuste PG: {bonos_con['ajuste_dg']:>2} | Shock: {bonos_con['shock']}% | Resurrección: {bonos_con['resurreccion']}% | Regen: {bonos_con['regen']}")
print(f"INT: {inteligencia_pj:<2} | Lenguajes: {bonos_int['lenguajes']:>2} | Máx. Nivel: {bonos_int['nivel_max']} | Prob. Aprender: {bonos_int['prob_aprender']}% | Máx. Conjuros: {bonos_int['max_conjuros']} | Inmunidad conjuros: {bonos_int['inm_ilusion']}")
print(f"SAB: {sabiduria_pj:<2} | Defensa Mágica: {bonos_sab['defensa']:>2} | Conjuros Bono: {bonos_sab['bonos']} | Fracaso: {bonos_sab['fracaso']}%")
if bonos_sab['inmunidad'] != "Ninguna":
    print(f"      [ INMUNIDAD MENTAL: {bonos_sab['inmunidad']} ]")
print(f"CAR: {carisma_pj:<2} | Máx. Seguidores: {bonos_car['max_seg']:>2} | Lealtad: {bonos_car['lealtad_bas']:>2} | Reacción: {bonos_car['ajuste_rc']:>2}")
print("="*55)