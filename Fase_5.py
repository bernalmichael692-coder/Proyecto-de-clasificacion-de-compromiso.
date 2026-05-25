# Formato: [ID Cliente, Duración (segundos), Eventos Clics]
matriz_sesiones = [
    [101, 200, 10],  
    [102, 45, 5],    
    [103, 150, 5],   
    [104, 300, 2],    
    [105, 120, 9]    
]

# Módulo (Función) 
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8: 
        return "Alto" # Clasificación "Alto"
    
    elif duracion < 60 or clics < 3:
        return "Bajo" # Clasificación "Bajo"
    
    else:
        return "Medio" # Clasificación "Medio": Todos los demas casos

# Calculo clasificacion de compromiso
print("="*40)
print("--- INFORME COMPROMISO DE SESIONES ---")
print("="*40)
print("ID CLIENTE\tCLASIFICACIÓN FINAL")
print("="*40)

for sesion in matriz_sesiones: 
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    
    clasificacion = clasificar_compromiso(duracion, clics) 
    
    print(f"{id_cliente}\t\t{clasificacion}") 