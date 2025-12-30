# Tabla de bonificadores de Fuerza 
# Estructura: valor: (ajuste_ataque, ajuste_daño)
def calcular_bonos_fuerza(valor, clase, porcentaje=0):
    if valor == 18:
        if clase.lower() != "guerrero":
            return {"golpe": 1, "ajuste_daño": 2, "desc": "18 Normal"}
        
        if 1 <= porcentaje <= 50:
            return {"golpe": 1, "ajuste_daño": 3, "desc": "18/01-50"}
        elif 51 <= porcentaje <= 75:
            return {"golpe": 2, "ajuste_daño": 3, "desc": "18/51-75"}
        elif 76 <= porcentaje <= 90:
            return {"golpe": 2, "ajuste_daño": 4, "desc": "18/76-90"}
        elif 91 <= porcentaje <= 99:
            return {"golpe": 2, "ajuste_daño": 5, "desc": "18/91-99"}
        elif porcentaje == 100:
            return {"golpe": 3, "ajuste_daño": 6, "desc": "18/00 (¡Bestial!)"}
    
    return {"golpe": 0, "ajuste_daño": 0, "desc": "Fuerza estándar"}

# 1. Pedir el Nombre (Esto es texto, no necesita int)
nombre_pj = input("¿Cual es el nombre de tu heroe? ")

# 2. Pedimos la clase
clase_pj = input("¿Cual es la clase de tu personaje? (Guerrero, Mago, etc.): ")

# 3. Pedimos la fuerza
fuerza_pj = int(input("¿Que fuerza tiene? (3-18): "))

# Aquí aplicamos TU lógica:
porcentaje_pj = 0
# Solo si es Guerrero (Luchador) Y tiene 18, pedimos porcentaje
if fuerza_pj == 18 and clase_pj.lower() == "guerrero":
    porcentaje_pj = int(input("¡Fuerza excepcional de Guerrero! Poné el porcentaje (1-100): "))

# 4. Cálculo de los bonos
bonos = calcular_bonos_fuerza(fuerza_pj, clase_pj, porcentaje_pj)

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
print(f"FUE: {fuerza_texto:<7} Probab. Golpe: +{bonos['golpe']}   Ajuste Daño: +{bonos['ajuste_daño']}")
print("="*55)