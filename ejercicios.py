# =====================================================================
#  ejercicios.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#  Aquí van TODOS los ejercicios del módulo 📋 Listas de la guía:
#     • 3 ejercicios DESARROLLADOS (taller paso a paso)  -> T1, T2, T3
#     • 5 ejercicios PROPUESTOS (solución oculta)         -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que:
#     1) imprime su enunciado corto,
#     2) usa datos fijos de prueba (los indicados en cada función),
#     3) muestra el resultado.
#
#  REGLA: en cada ejercicio resuelve con DOS versiones cuando se indique:
#     ✋ MANUAL (bucles, patrones del módulo 0)  y  🐍 PYTHON (built-ins
#     y comprensiones). Imprime ambas para comparar.
#  Cuando termines una función, BORRA la línea "pass".
# =====================================================================


# ============================ DESARROLLADOS ==========================

def ejercicio_t1():
   
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero

    print("=== INICIO DE LA DEMOSTRACIÓN ===")

    
    lista = ListaPasajerosPython()
    
    p1 = Pasajero("0911111111", "Carlos", 25)
    p2 = Pasajero("0922222222", "Ana", 30)
    p3 = Pasajero("0933333333", "Beatriz", 22)

    lista.añadir(p1)
    lista.añadir(p2)
    lista.añadir(p3)

   
    print("\n--- 1. LISTA INICIAL ---")
    lista.listar()

   
    print("\n--- 2. BUSCAR PASAJERO (Cédula: 0922222222) ---")
    pos = lista.buscar("0922222222")
    print(f"Encontrado en la posición: {pos}")

   
    print("\n--- 3. MODIFICAR PASAJERO ---")
    lista.modificar("0922222222", "Ana María", 31)
    lista.listar()

   
    print("\n--- 4. ELIMINAR PASAJERO (Cédula: 0911111111) ---")
    lista.eliminar_por_valor("0911111111")

  
    print("\n--- 5. LISTA DESPUÉS DE ELIMINAR ---")
    lista.listar()


    print("\n--- 6. RETO: ORDENAR POR NOMBRE (A-Z) ---")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    lista.listar()

  

def ejercicio_t2():
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

   
    promedio = sum(notas) / len(notas)
    
    min_nota = min(notas)
    max_nota = max(notas)
    
    indice_mejor = notas.index(max_nota)
    nombre_mejor = nombres[indice_mejor]

    aprobados = [n for n in notas if n >= 7]
    cantidad_aprobados = len(aprobados)
    total_estudiantes = len(notas)


    print(f"Promedio {promedio:.2f} · Máx {max_nota} ({nombre_mejor}) · Mín {min_nota} · Aprobados {cantidad_aprobados} de {total_estudiantes}")



def ejercicio_t3():

    numeros = [5, 2, 8, 1, 9, 3, 7]
    print(f"Lista original: {numeros}")

   
    copia = numeros[:]
    n = len(copia)
    
    for i in range(n):
        hubo_swap = False
        for j in range(0, n - i - 1):
            if copia[j] > copia[j + 1]:
            
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                hubo_swap = True
        
       
        if not hubo_swap:
            break

    print(f"Manual (Bubble Sort ordenado): {copia}")

   
    ascendente_python = sorted(numeros)
    print(f"Python (sorted ascendente): {ascendente_python}")
    
   
    descendente_python = numeros.copy()
    descendente_python.sort(reverse=True)
    print(f"Python (.sort descendente): {descendente_python}")

   
    palabras = ["python", "a", "código", "el"]
    palabras_ordenadas = sorted(palabras, key=len)
    print(f"Extra (palabras por longitud): {palabras_ordenadas}")

# ============================= PROPUESTOS ============================

def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3

    # 1. MANUAL 
    contador = 0
    for x in lista:
        if x == v:
            contador += 1

    # 2. PYTHON 
    # python_count = lista.count(v)

    # 3. COMPRENSIÓN
    # comp_count = len([x for x in lista if x == v])

    print(f"Salida esperada: {v} aparece {contador} veces")


def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    lista = [1, 2, 3, 4, 5]

    # 1. MANUAL 
    invertida_manual = []
    for i in range(len(lista) - 1, -1, -1):
        invertida_manual.append(lista[i])

    # 2. PYTHON 
    # invertida_python = lista[::-1]
    #list(reversed(lista)

    # 3. COMPRENSIÓN
    # invertida_comp = [lista[i] for i in range(len(lista) - 1, -1, -1)]

    print(f"Salida esperada: {invertida_manual}")
    # print(f"Python (.count): {python_count} veces")
    # print(f"Comprensión: {comp_count} veces")


def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
                NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    nums = [1, 3, 2, 3, 4, 1, 5, 2]

    # 1. MANUAL
    unicos_manual = []
    for n in nums:
        if n not in unicos_manual:
            unicos_manual.append(n)

    # 2. PYTHON 
    # unicos_python = list(dict.fromkeys(nums))
    
    print(f"Salida esperada: {unicos_manual}")


def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    nums = [5, 2, 9, 7, 9, 3, 8]

    # MANUAL
    mayor = float('-inf')
    segundo = float('-inf')

    for n in nums:
        if n > mayor:
            segundo = mayor
            mayor = n
        elif n > segundo and n != mayor:
            segundo = n

    print(f"Salida esperada: Mayor {mayor} · Segundo {segundo}")    


def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
               y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]

    # MANUAL
    i = 0
    j = 0
    fusionada = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            fusionada.append(a[i])
            i += 1
        else:
            fusionada.append(b[j])
            j += 1

    fusionada.extend(a[i:])
    fusionada.extend(b[j:])

    print(f"Salida esperada: {fusionada}")

# ============================== CATÁLOGO =============================
def menu_ejercicios():
    """
    QUÉ HACE : muestra los ejercicios agrupados y ejecuta el que elija
                 el usuario, hasta que escriba 0.
    PASOS    :
      1. Con COMPRENSIONES separa el catálogo:
               taller     = [e for e in EJERCICIOS if e[2] == "taller"]
               propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
      2. Muestra:
               --- DESARROLLADOS (taller) ---
                 T1. CRUD de pasajeros ...
               --- PROPUESTOS ---
                 P1. Contar apariciones ...
                 0.  Volver
      3. Lee el código (ej. "t2") y pásalo a mayúsculas con .upper().
      4. Busca la tupla con ese código (otra comprensión o next(...)):
               encontrados = [e for e in EJERCICIOS if e[0] == codigo]
      5. Si existe -> llama a su función:  encontrados[0][3]()
         Si no     -> "Código no válido".
      6. Repite hasta que el usuario escriba "0".
    """
    EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
    ]
    
    taller = [e for e in EJERCICIOS if e[2] == "taller"]
    propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]

    while True:
       
        print("\n" + "=" * 45)
        print("           MENÚ DE EJERCICIOS Y TALLERES")
        print("=" * 45)
        
        print("--- DESARROLLADOS (taller) ---")
        for codigo, titulo, tipo, func in taller:
            print(f"  {codigo}. {titulo}")

        print("\n--- PROPUESTOS ---")
        for codigo, titulo, tipo, func in propuestos:
            print(f"  {codigo}. {titulo}")
            
        print("  0.  Volver")
        print("-" * 45)

        
        codigo_ingresado = input("Elige el código del ejercicio a ejecutar: ").strip().upper()

       
        if codigo_ingresado == "0":
            print("\n👋 ¡Volviendo al menú principal. Hasta luego!")
            break

       
        encontrados = [e for e in EJERCICIOS if e[0] == codigo_ingresado]

        
        if encontrados:
            ejercicio = encontrados[0]
            print(f"\n Ejecutando [{ejercicio[0]}] - {ejercicio[1]}...\n")
            
           
            ejercicio[3]()
            
            print("\n" + "=" * 45)
            input("Presiona ENTER para continuar...")
        else:
            print("\n⚠ Código no válido. Por favor, verifica e intenta de nuevo.")