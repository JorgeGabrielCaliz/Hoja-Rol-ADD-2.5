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

TABLA_HABILIDADES_RACIALES = {
    "enano": [
        "Infravisión 18m",
        "Detección de trabajos de cantería (trampas, muros falsos, etc.)",
        "+1 al ataque contra Orcos, Medio-Orcos, Trasgos y Hobgoblins",
        "Los gigantes/ogros tienen -4 para golpearte",
        "Resistencia mágica: +1 a salvación por cada 3.5 puntos de CON"
    ],
    "elfo": [
        "Infravisión 18m",
        "90% ", "resistencia a Dormir y Encantamiento",
        "+1 al ataque con espadas largas, cortas y arcos (no ballestas)",
        "Bonificador al movimiento sigiloso si no visten armadura metálica",
        "Detectar puertas secretas/ocultas al pasar cerca"
    ],
    "halfling": [ # O "mediano" según tu lista
        "Bonificador al ataque con hondas y armas arrojadizas",
        "Sorprender enemigos (sigilo)",
        "Resistencia mágica: +1 a salvación por cada 3.5 puntos de CON"
    ],
    "gnomo": [
        "Infravisión 18m",
        "Detección de túneles e inclinaciones",
        "Resistencia mágica: +1 a salvación por cada 3.5 puntos de CON",
        "+1 al ataque contra Kobolds y Trasgos"
    ],
    "humano": ["Habilidad de Clase Dual", "Sin penalizadores ni bonos específicos"],
    "semielfo": ["Infravisión 18m", "30%", " resistencia a Dormir y Encantamiento"]
}

# --- TABLA DE CLASES (Manual del Jugador 2.5) ---
TABLA_CLASES = {
    # LUCHADORES
    "guerrero":   {"req": {"FUE": 9}, "die": 10, "grupo": "luchador"},
    "paladin":    {"req": {"FUE": 12, "CON": 9, "SAB": 13, "CAR": 17}, "die": 10, "grupo": "luchador"},
    "explorador": {"req": {"FUE": 13, "DES": 13, "CON": 14, "SAB": 14}, "die": 10, "grupo": "luchador"},
    
    # HECHICERO
    "hechicero":       {"req": {"INT": 9}, "die": 4, "grupo": "mago"},
    
    # SACERDOTES
    "clerigo":    {"req": {"SAB": 9}, "die": 8, "grupo": "sacerdote"},
    "druida":     {"req": {"SAB": 12, "CAR": 15}, "die": 8, "grupo": "sacerdote"},
    
    # BRIBONES
    "ladron":     {"req": {"DES": 9}, "die": 6, "grupo": "picaro"},
    "bardo":      {"req": {"DES": 12, "INT": 13, "CAR": 15}, "die": 6, "grupo": "picaro"}
}

DADOS_VIDA = {
    "luchador": 10,
    "sacerdote": 8,
    "bribon": 6,
    "hechicero": 4
}
# --- TABLA DE FUERZA ---
TABLA_FUE = {
    1:  (-5, -4, 1, 2, "1", 0, ""),
    2:  (-3, -2, 1, 3, "1", 0, ""),
    3:  (-3, -1, 3, 5, "2", 0, ""),
    4:  (-2, -1, 5, 23, "3", 0, ""),
    5:  (-2, -1, 5, 23, "3", 0, ""),
    6:  (-1, 0, 10, 28, "4", 0, ""),
    7:  (-1, 0, 10, 28, "4", 0, ""),
    8:  (0, 0, 18, 45, "5", 1, ""),
    10: (0, 0, 20, 58, "6", 2, ""),
    12: (0, 0, 23, 70, "7", 4, ""),
    14: (0, 0, 28, 85, "8", 7, ""),
    16: (0, 1, 35, 98, "9", 10, ""),
    17: (1, 1, 43, 110, "10", 13, ""),
    18: (1, 2, 55, 130, "11", 16, ""),
    # Fuerza Excepcional (Luchadores) 
    "18/50": (1, 3, 70, 140, "12", 20, "Excepcional"),
    "18/75": (2, 3, 80, 155, "13", 25, "Excepcional"),
    "18/90": (2, 4, 95, 165, "14", 30, "Excepcional"),
    "18/99": (2, 5, 120, 190, "15(3)", 35, "Excepcional"),
    "18/00": (3, 6, 170, 240, "16(6)", 40, "Bestial"), # El famoso 18/00
    # Fuerzas de Gigante (19+)
    19: (3, 7, 245, 320, "16(8)", 50, "Gigante Colinas"), # Gigante de las Colinas 
    20: (3, 8, 270, 350, "17(10)", 60, "Gigante Piedra"), # Gigante de Piedra 
    21: (4, 9, 320, 405, "17(12)", 70, "Gigante Escarchas"), # Gigante de las Escarchas 
    22: (4, 10, 395, 485, "18(14)", 80, "Gigante Fuego"), # Gigante de Fuego 
    23: (5, 11, 470, 565, "18(16)", 90, "Gigante Nubes"), # Gigante de las Nubes 
    24: (6, 12, 620, 720, "19(17)", 95, "Gigante Tormentas"), # Gigante de las Tormentas 
    25: (7, 14, 770, 875, "19(18)", 99, "Titán") # Titán 
}
# --- TABLA DE DESTREZA ---
TABLA_DES = {
    1: (-6, -6, +5),
    2: (-4, -4, +5),
    3: (-3, -3, +4),
    4: (-2, -2, +3),
    5: (-1, -1, +2),
    6: (0, 0, +1),
    7: (0, 0, 0),
    15: (0, 0, -1),
    16: (+1, +1, -2),
    17: (+2, +2, -3),
    18: (+2, +2, -4),
    19: (+3, +3, -4),
    21: (+4, +4, -5),
    23: (+4, +4, -5),
    24: (+5, +5, -6)
}
# TABLA DE CONSTITUCION
# Ajuste de Vida (Luchadores suben hasta +9, el resto capea en +2)
TABLA_CON_LUCHADOR = {
    1: -3, 2: -2, 4: -1, 7: 0, 15: 1, 16: 2, 17: 3, 18: 4,
    19: 5, 20: 5, 21: 6, 22: 6, 23: 6, 24: 7, 25: 7
}
TABLA_CON_ESTANDAR = {
    1: -3, 2: -2, 4: -1, 7: 0, 15: 1, 16: 2, 17: 2, 18: 2,
    19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2
}
# Shock y Resurrección (Llegan al 99% y 100% y se mantienen)
TABLA_SHOCK_SISTEMICO = {
    1: 25, 2: 30, 3: 35, 4: 40, 5: 45, 6: 50, 7: 55, 8: 60, 9: 65, 10: 70,
    11: 75, 12: 80, 13: 85, 14: 88, 15: 90, 16: 95, 17: 97, 18: 99, 
    19: 99, 20: 99, 21: 99, 22: 99, 23: 99, 24: 99, 25: 100
}
TABLA_SUPERVIVENCIA_RES = {
    1: 30, 2: 35, 3: 40, 4: 45, 5: 50, 6: 55, 7: 60, 8: 65, 9: 70, 10: 75,
    11: 80, 12: 85, 13: 90, 14: 92, 15: 94, 16: 96, 17: 98, 18: 100,
    19: 100, 20: 100, 21: 100, 22: 100, 23: 100, 24: 100, 25: 100
}
# Resistencia a venenos (desde el penalizadr hasta el +4)
TABLA_VENENO = {
    1: -2, 2: -1, 3: 0, 19: 1, 21: 2, 23: 3, 25: 4
}
# Regeneración (Este es el cambio más groso en niveles altos)
TABLA_REGEN = {
    20: "1/6 turnos",
    21: "1/5 turnos",
    22: "1/4 turnos",
    23: "1/3 turnos",
    24: "1/2 turnos",
    25: "1/1 turno"
}
# TABLA INTELIGENCIA
# Formato: (lenguajes, nivel_max_conjuro, prob_aprender, max_conjuros_por_nivel, inmunidad_ilusion)
TABLA_INT = {
    1:  (0, 0, 0, 0, "Ninguna"),
    2:  (1, 0, 0, 0, "Ninguna"),
    9:  (2, 4, 35, 6, "Ninguna"),
    10: (2, 5, 40, 7, "Ninguna"),
    12: (3, 6, 50, 7, "Ninguna"),
    13: (3, 6, 55, 9, "Ninguna"),
    14: (4, 7, 60, 9, "Ninguna"),
    15: (4, 7, 65, 11, "Ninguna"),
    16: (5, 8, 70, 11, "Ninguna"),
    17: (6, 8, 75, 14, "Ninguna"),
    18: (8, 9, 85, 18, "Ninguna"),
    19: (9, 9, 95, 99, "Ilusion 1er Nivel"),
    20: (10, 9, 96, 99, "Ilusion 2do Nivel"),
    21: (11, 9, 97, 99, "Ilusion 3er Nivel"),
    22: (12, 9, 98, 99, "Ilusion 4to Nivel"),
    23: (13, 9, 99, 99, "Ilusion 5to Nivel"),
    24: (15, 9, 100, 99, "Ilusion 6to Nivel"),
    25: (20, 9, 100, 99, "Ilusion 7mo Nivel")
}
# TABLA SABIDURIA
# Formato: (defensa_magica, conjuros_bono, probabilidad_fallo, inmunidades)
TABLA_SAB = {
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
    19: (+4, "1,4", 0, "Causa miedo, Encantamiento de persona, Autoridad, Amigos, Hipnotismo"),
    20: (+4, "2,4", 0, "Olvidar, Retencion de personas, Rayo debilitador, Intimidacion"),
    21: (+4, "3,5", 0, "Miedo"),
    22: (+4, "4,5", 0, "Encantamiento de monstruo, Confusion, Emocion, Tanteo, Sugestion"),
    23: (+4, "5,5", 0, "Caos, Debilidad mental, Retencion de personalidad, Frasco magico, Busqueda"),
    24: (+4, "6,6", 0, "Geas, Sugestion de masas, Varita de liderazgo"),
    25: (+4, "6,7", 0, "Antipatia/simpatia, Conjuro de muerte, Encantamiento de masas")
}
# TABLA CARISMA
# Formato: (max_seguidores, lealtad_base, ajuste_reaccion)
TABLA_CAR = {
    1: (0, -8, -7),
    2: (1, -7, -6),
    3: (1, -6, -5),
    4: (1, -5, -4),
    5: (2, -4, -3),
    6: (2, -3, -2),
    7: (3, -2, -1),
    8: (3, 0, 0),
    9: (4, 0, 0),
    12: (5, 0, 0),
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
# --- TABLAS DE SALVACIÓN ---
# (Paralización/Veneno, Vara/Vara/Cetro, Petrificación, Arma de Aliento, Conjuro)
TS_LUCHADOR = {
    1: (14, 16, 15, 17, 17),
    3: (13, 15, 14, 16, 16),
    5: (11, 13, 12, 13, 14),
    7: (10, 12, 11, 12, 13),
    9: (8, 10, 9, 9, 11),
    11: (7, 9, 8, 8, 10),
    13: (5, 7, 6, 5, 8),
    15: (4, 6, 5, 4, 7),
    17: (3, 5, 4, 4, 6)
}

TS_SACERDOTE = {
    1: (10, 14, 13, 16, 15),
    4: (9, 13, 12, 15, 14),
    7: (7, 11, 10, 13, 12),
    10: (6, 10, 9, 12, 11),
    13: (5, 9, 8, 11, 10),
    16: (4, 8, 7, 10, 9),
    19: (2, 6, 5, 8, 7)
}

TS_HECHICERO = {
    1: (14, 11, 13, 15, 12),
    6: (13, 9, 11, 13, 10),
    11: (11, 7, 9, 11, 8),
    16: (10, 5, 7, 9, 6),
    21: (8, 3, 5, 7, 4)
}

TS_BRIBON = {
    1: (13, 14, 12, 16, 15),
    5: (12, 12, 11, 15, 14),
    9: (11, 10, 10, 14, 13),
    13: (10, 8, 9, 13, 12),
    17: (9, 6, 8, 12, 11),
    21: (8, 4, 7, 11, 10)
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

def validar_clase_pj(clase, mis_atribs, habilitado, soltura):
    """
    clase: el nombre de la clase elegida.
    mis_atribs: un diccionario con los valores finales del PJ.
    habilitado: el interruptor 'validar_clases'.
    soltura: el interruptor 'soltura_master'.
    """
    if not habilitado: 
        return True # Si no validamos, siempre pasa
    
    nombre_clase = clase.lower()
    if nombre_clase not in TABLA_CLASES:
        print(f"❌ ERROR: La clase '{clase}' no existe en el manual.")
        return False # Si la clase no está en la lista o esta inventada, no podemos validarla
    
    requisitos = TABLA_CLASES[nombre_clase]["req"]
    cumple_todo = True
    
    print(f"\n--- Chequeando vocación de {clase.capitalize()} ---")
    
    for atrib, min_req in requisitos.items():
        valor_pj = mis_atribs.get(atrib, 0)
        if valor_pj < min_req:
            print(f"❌ REQUISITO FALLIDO: {atrib} mínimo {min_req} (Tienes {valor_pj})")
            cumple_todo = False
        else:
            print(f"✅ {atrib} correcto.")

    if not cumple_todo:
        if soltura:
            print(">>> ADVERTENCIA: No cumples los requisitos, pero el Master permite excepciones.")
            return True
        else:
            print(">>> BLOQUEO: Este personaje no es legal según las reglas oficiales.")
            return False
    
    print(">>> ¡Cumples con todos los requisitos de clase!")
    return True


def buscar_en_tabla(tabla, val):
    # Si el valor es un string (como 18/50), lo devolvemos directo
    if val in tabla: return tabla[val]
    # Si es número, buscamos el anterior más cercano
    claves = sorted([k for k in tabla.keys() if isinstance(k, int) and k <= val])
    return tabla[claves[-1]] if claves else tabla[min(tabla.keys())]

# Tabla de bonificadores de Fuerza
def calcular_bonos_fuerza(valor, grupo, porcentaje=0):
    v = max(1, min(25, valor))
    clave = v
    
    # Lógica para el 18 excepcional
    if v == 18 and grupo.lower() == "luchador":
        if 1 <= porcentaje <= 50: clave = "18/50"
        elif 51 <= porcentaje <= 75: clave = "18/75"
        elif 76 <= porcentaje <= 90: clave = "18/90"
        elif 91 <= porcentaje <= 99: clave = "18/99"
        elif porcentaje == 100: clave = "18/00"
    
    res = buscar_en_tabla(TABLA_FUE, clave)
    return {
        "golpe": res[0], "ajuste_daño": res[1], "peso_perm": res[2],
        "esfuerzo_max": res[3], "abrir_puertas": res[4], "barras_rejas": res[5], "nota": res[6]
    }

def calcular_bonos_destreza(valor):
    v = max(1, min(25, valor))
    res = buscar_en_tabla(TABLA_DES, v)
    return {
        "ajuste_rc": res[0], "ajuste_proy": res[1], "ajuste_def": res[2]
    }

def calcular_bonos_constitucion(valor, grupo_mecanico, raza="Humano"):
    # Limitar el valor para que no se pase de 25 ni baje de 1
    v = max(1, min(25, valor))
    
    # 1. Ajuste de Vida: usamos .get con lógica de "caída"
    # Buscamos el valor más alto en la tabla que sea menor o igual a 'v'
    def buscar_en_tabla(tabla, val):
        claves = sorted([k for k in tabla.keys() if k <= val])
        return tabla[claves[-1]] if claves else 0

    if grupo_mecanico.lower() == "luchador":
        bono_vida = buscar_en_tabla(TABLA_CON_LUCHADOR, v)
    else:
        bono_vida = buscar_en_tabla(TABLA_CON_ESTANDAR, v)
        
    # 2. Shock y Resurrección
    shock = buscar_en_tabla(TABLA_SHOCK_SISTEMICO, v)
    res = buscar_en_tabla(TABLA_SUPERVIVENCIA_RES, v)
    
    # 3. Veneno (Ahora para todos + bono racial)
    
    # Primero: Calculamos el bono estándar que estás haciendo vos (para todas las razas)
    # Suponiendo que tu tabla se llama TABLA_VENENO_ESTANDAR
    bono_veneno_base = buscar_en_tabla(TABLA_VENENO, v)
    
    # Segundo: Si es Enano/Mediano, calculamos su bono EXTRA
    bono_racial = 0
    if raza.lower() in ["enano", "mediano", "halfling"]:
        # Esta es la tabla de bonos extras por CON (la de +1 cada 3.5 puntos)
        tabla_extra = {1: 0, 4: 1, 7: 2, 11: 3, 14: 4, 18: 5}
        bono_racial = buscar_en_tabla(tabla_extra, v)

    # Sumamos ambos
    total_veneno = bono_veneno_base + bono_racial
    
    # 4. Regeneración
    regen = TABLA_REGEN.get(v, "Ninguna")

    return {
        "vida": bono_vida,
        "shock": shock,
        "res": res,
        "veneno": total_veneno,
        "regen": regen
    }

def calcular_bonos_inteligencia(valor):
    v = max(1, min(25, valor))
    
    # Buscamos el valor más alto en la tabla que sea menor o igual a 'v'
    claves = sorted([k for k in TABLA_INT.keys() if k <= v])
    res = TABLA_INT[claves[-1]]

    return {
        "lenguajes": res[0], 
        "nivel_max": res[1], 
        "prob_aprender": f"{res[2]}%", 
        "max_conjuros": res[3], 
        "inm_ilusion": res[4]
    }

def calcular_bonos_sabiduria(valor):
    v = max(1, min(25, valor))
    
    # Buscamos en tu TABLA_SAB (la que completaste vos)
    claves = sorted([k for k in TABLA_SAB.keys() if k <= v])
    res = TABLA_SAB[claves[-1]]

    return {
        "defensa": res[0],
        "bonos": res[1],
        "fracaso": res[2],
        "inmunidad": res[3]
    }

def calcular_bonos_carisma(valor):
    v = max(1, min(25, valor))
    
    # Buscamos en tu TABLA_CAR
    claves = sorted([k for k in TABLA_CAR.keys() if k <= v])
    res = TABLA_CAR[claves[-1]]

    return {
        "max_seg": res[0],
        "lealtad_bas": res[1],
        "ajuste_rc": res[2]
    }

def calcular_pg_totales(vida_dados, nivel, bono_con):
    # El bono de constitución se aplica por cada nivel (hasta nivel 9/10 generalmente)
    # Por ahora lo hacemos lineal:
    vida_por_con = nivel * bono_con
    total = vida_dados + vida_por_con
    
    return total, vida_por_con

def calcular_salvaciones_base(nivel, grupo):
    # Diccionario para elegir la tabla correcta
    tablas = {
        "luchador": TS_LUCHADOR,
        "sacerdote": TS_SACERDOTE,
        "hechicero": TS_HECHICERO,
        "bribon": TS_BRIBON
    }
    
    # Seleccionamos la tabla, si no encuentra usa luchador por defecto
    tabla_elegida = tablas.get(grupo, TS_LUCHADOR)
    
    # Buscamos el escalón de nivel (lógica de caída que ya usamos)
    claves = sorted([k for k in tabla_elegida.keys() if k <= nivel])
    base = tabla_elegida[claves[-1]]
    
    return {
        "veneno": base[0],
        "varas": base[1],
        "petri": base[2],
        "aliento": base[3],
        "conjuro": base[4]
    }

# --- FLUJO PRINCIPAL ---

# --- INTERRUPTORES RAZAS Y CLASES---
validar_topes = input("¿Validar límites de Atributos por Raza? (S/N): ").upper() == "S"
validar_clases = input("¿Validar requisitos mínimos para Clases? (S/N): ").upper() == "S"
soltura_master = input("¿Modo Ambientación (solo avisar)? (S/N): ").upper() == "S"

# 1. Datos básicos
print("\n" + "="*40)
nombre_pj = input("¿Cuál es el nombre de tu héroe? ")
raza_pj = input("¿Cuál es tu raza? (Humano, Elfo, etc.): ").lower()
clase_pj = input("¿Cuál es tu profesión específica? (Ej: Caballero de Solamnia): ")

# AQUÍ EL NUEVO SELECTOR
print("\n--- Selecciona el Grupo Mecánico ---")
print("1. Luchador  (Fuerza Excepcional, Dados de Golpe d10)")
print("2. Hechicero      (Dados de Golpe d4)")
print("3. Sacerdote (Dados de Golpe d8)")
print("4. Bribón    (Dados de Golpe d6)")
opcion = input("Elegí el grupo (1-4): ")

# Mapeo de la elección
diccionario_grupos = {"1": "luchador", "2": "hechicero", "3": "sacerdote", "4": "bribon"}
grupo_pj = diccionario_grupos.get(opcion, "luchador") # Por defecto luchador
print("="*40 + "\n")

# --- 2. PEDIR ATRIBUTOS Y APLICAR BONOS EN EL MOMENTO ---

# Primero necesitamos los bonos de raza para los cálculos en tiempo real
bonos_raza = TABLA_RAZAS.get(raza_pj, {"FUE": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0})
porcentaje_pj = 0
# FUERZA
fuerza_base = int(input("Fuerza base: "))
validar_y_avisar("FUE", fuerza_base, raza_pj, validar_topes, soltura_master)
fuerza_pj = fuerza_base + bonos_raza.get("FUE", 0)
# Simplificado: Si el grupo es luchador y tiene 18, pide el porcentaje
if fuerza_pj == 18 and grupo_pj == "luchador":
    porcentaje_pj = int(input(f"¡Fuerza excepcional! Tirada de 1d100: "))
# DESTREZA
destreza_base = int(input("Destreza base: "))
validar_y_avisar("DES", destreza_base, raza_pj, validar_topes, soltura_master)
destreza_pj = destreza_base + bonos_raza.get("DES", 0)
# CONSTITUCION
constitucion_base = int(input("Constitucion base: "))
validar_y_avisar("CON", constitucion_base, raza_pj, validar_topes, soltura_master)
constitucion_pj = constitucion_base + bonos_raza.get("CON", 0)
# INTELIGENCIA
inteligencia_base = int(input("Inteligencia base: "))
validar_y_avisar("INT", inteligencia_base, raza_pj, validar_topes, soltura_master)
inteligencia_pj = inteligencia_base + bonos_raza.get("INT", 0)
# SABIDURIA
sabiduria_base = int(input("Sabiduria base: "))
validar_y_avisar("SAB", sabiduria_base, raza_pj, validar_topes, soltura_master)
sabiduria_pj = sabiduria_base + bonos_raza.get("SAB", 0)
# CARISMA
carisma_base = int(input("Carisma base: "))
validar_y_avisar("CAR", carisma_base, raza_pj, validar_topes, soltura_master)
carisma_pj = carisma_base + bonos_raza.get("CAR", 0)

# Armamos el diccionario para la validación de clase
mis_atribs_finales = {
    "FUE": fuerza_pj, "DES": destreza_pj, "CON": constitucion_pj,
    "INT": inteligencia_pj, "SAB": sabiduria_pj, "CAR": carisma_pj
}

es_legal = validar_clase_pj(clase_pj, mis_atribs_finales, validar_clases, soltura_master)
# Si no es legal y NO tenemos soltura, frenamos el programa
if not es_legal and not soltura_master:
    print("\n[!] No puedes continuar con un personaje ilegal.")
    exit() # Esto cierra el programa para que el usuario tenga que empezar de nuevo
elif not es_legal and soltura_master:
    input("\n⚠️  Atención: Se aplicarán reglas caseras. Presioná Enter para confirmar...")
# ------------------------------

# 4. Cálculo de los bonos
bonos_fue = calcular_bonos_fuerza(fuerza_pj, grupo_pj, porcentaje_pj)
bonos_des = calcular_bonos_destreza(destreza_pj)
bonos_con = calcular_bonos_constitucion(constitucion_pj, grupo_pj, raza_pj)
bonos_int = calcular_bonos_inteligencia(inteligencia_pj)
bonos_sab = calcular_bonos_sabiduria(sabiduria_pj)
bonos_car = calcular_bonos_carisma(carisma_pj)

# --- En la parte principal del código ---
nivel_pj = int(input(f"¿Qué nivel es tu {clase_pj}?: "))
dado = DADOS_VIDA.get(grupo_pj, 10)

print(f"\n[SISTEMA] Al ser nivel {nivel_pj}, debes lanzar {nivel_pj}d{dado}.")
vida_sacada = int(input("Introduce el total sumado de tus dados: "))

# Calculamos
pg_finales, vida_bonus_con = calcular_pg_totales(vida_sacada, nivel_pj, bonos_con["vida"])

# --- SECCIÓN DE PREPARACIÓN PARA LA FICHA ---

# 1. Preparamos el texto del número (18/00, etc)
if porcentaje_pj > 0:
    fuerza_texto = f"{fuerza_pj}/{'00' if porcentaje_pj == 100 else porcentaje_pj}"
else:
    fuerza_texto = f"{fuerza_pj}"

# 2. Preparamos la nota (lo que me preguntaste recién)
nota_fuerza = f" ({bonos_fue['nota']})" if bonos_fue['nota'] else ""
ts_base = calcular_salvaciones_base(nivel_pj, grupo_pj)

# 3. Limpiamos pantalla y dibujamos la ficha
os.system('cls' if os.name == 'nt' else 'clear')
# LA LÍNEA MÁGICA DE LA HOJA
print("\n" + "="*55)
print(f" FICHA DE PERSONAJE: {nombre_pj.upper()} ")
print("="*55)
print(f"CLASE: {clase_pj.capitalize()} | RAZA: {raza_pj.capitalize()} | NIVEL: {nivel_pj}")
print(f"PUNTOS DE GOLPE: {pg_finales} ({vida_sacada} puntos + {vida_bonus_con} Constitución)")
print(f"{'ATRIBUTO':<10} | {'VALOR':<10}")
print("-" * 55)
fuerza_texto: print(f"FUE: {fuerza_texto:<7} | Golpe: {bonos_fue['golpe']:>2} | Daño: {bonos_fue['ajuste_daño']:>2} | Carga: {bonos_fue['peso_perm']:>2}/{bonos_fue['esfuerzo_max']:>2} | Puertas: {bonos_fue['abrir_puertas']:>3} | Barras: {bonos_fue['barras_rejas']:>2}%{nota_fuerza}")
print(f"DES: {destreza_pj:<2} | Reacción: {bonos_des['ajuste_rc']:>2} | Proyectiles: {bonos_des['ajuste_proy']:>2} | Defensa: {bonos_des['ajuste_def']:>2}")
print(f"CON: {constitucion_pj:<2} | Ajuste PG: {bonos_con['vida']:>2} | Shock: {bonos_con['shock']}% | Resurrección: {bonos_con['res']}% | Veneno: +{bonos_con['veneno']} | Regen: {bonos_con['regen']}")
print(f"INT: {inteligencia_pj:<2} | Lenguajes: {bonos_int['lenguajes']:>2} | Máx. Nivel: {bonos_int['nivel_max']} | Prob. Aprender: {bonos_int['prob_aprender']}% | Máx. Conjuros: {bonos_int['max_conjuros']} | Inmunidad conjuros: {bonos_int['inm_ilusion']}")
print(f"SAB: {sabiduria_pj:<2} | Defensa Mágica: {bonos_sab['defensa']:>2} | Conjuros Bono: {bonos_sab['bonos']} | Fracaso: {bonos_sab['fracaso']}%")
if bonos_sab['inmunidad'] != "Ninguna":
    print(f"      [ INMUNIDAD MENTAL: {bonos_sab['inmunidad']} ]")
print(f"CAR: {carisma_pj:<2} | Máx. Seguidores: {bonos_car['max_seg']:>2} | Lealtad: {bonos_car['lealtad_bas']:>2} | Reacción: {bonos_car['ajuste_rc']:>2}")
print("="*55)

# --- SECCIÓN DE HABILIDADES RACIALES (El cartel luminoso) ---
print("\n" + "!"*20 + " HABILIDADES RACIALES " + "!"*20)
habilidades = TABLA_HABILIDADES_RACIALES.get(raza_pj.lower(), ["No se encontraron habilidades."])

for hab in habilidades:
    print(f" > {hab}")
print("!" * 62)

print("\n" + "-"*15 + " TIRADAS DE SALVACIÓN (BASE) " + "-"*15)
print(f" P.Veneno: {ts_base['veneno']:>2} | Varas/Cetro: {ts_base['varas']:>2} | Petrif.: {ts_base['petri']:>2}")
print(f" Aliento : {ts_base['aliento']:>2} | Conjuros   : {ts_base['conjuro']:>2}")

# Notas de ayuda para el jugador (esto es lo que decíamos)
print("-" * 59)
print(f" NOTAS: Sabiduría otorga {bonos_sab['defensa']} contra efectos mentales.")
if raza_pj.lower() in ["enano", "halfling", "gnomo"]:
    # Calculamos el bono racial rápido para la nota
    bono_duro = int(constitucion_pj / 3.5)
    print(f" BONO RACIAL: +{bono_duro} contra Veneno y Varas (por CON).")
    
print("="*55)