# =====================================================================
#   main.py  —  PROGRAMA PRINCIPAL (menú de opciones)
# ---------------------------------------------------------------------
#   Ejecutar desde la carpeta del proyecto:     python main.py
# =====================================================================

from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios

# Las dos listas viven durante todo el programa
lista1 = ListaPasajerosManual(capacidad=10)
lista2 = ListaPasajerosPython()

PENDIENTE = "⚠ Opción por implementar (revisa el # TODO en main.py)"


# =========================== FUNCIONES DE APOYO ======================

def leer_entero(mensaje):
    """Pide un número entero y repite hasta que sea válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    """Pide los datos por teclado y retorna un objeto Pasajero."""
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula (10 dígitos): ").strip()
    edad = leer_entero("  Edad: ")
    return Pasajero(nombre, cedula, edad)


def cargar_datos_prueba(lista):
    """Carga 5 pasajeros de prueba. Funciona con LAS DOS listas
    porque ambas tienen el método añadir()."""
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana",   "0912345678", 28))
    lista.añadir(Pasajero("Luis",  "0987654321", 35))
    lista.añadir(Pasajero("Beto",  "0934567890", 16))
    lista.añadir(Pasajero("Elena", "0901234567", 41))
    print("  ✓ 5 pasajeros de prueba cargados")


def mostrar_menu_lista(titulo):
    """Mismo menú para las dos listas (mismas opciones)."""
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir pasajero (al final)")
    print(" 2. Listar pasajeros")
    print(" 3. Insertar en una posición")
    print(" 4. Buscar por cédula (lineal)")
    print(" 5. Buscar por cédula (binaria)")
    print(" 6. Modificar pasajero")
    print(" 7. Eliminar por posición")
    print(" 8. Eliminar por cédula (valor)")
    print(" 9. Ordenar ascendente (por cédula)")
    print("10. Ordenar descendente (por cédula)")
    print("11. Reversar")
    print("12. Copiar lista")
    print("13. Longitud")
    print("14. Filtrar mayores de edad")
    print("15. Nombres en mayúsculas")
    print(" C. Cargar datos de prueba")
    print(" 0. Volver")


# ============================ SUBMENÚ LISTA 1 ========================

def menu_lista1():
    while True:
        mostrar_menu_lista("LISTA 1 · desde cero")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista1.añadir(pasajero):
                print("Pasajero añadido")

        elif op == "2":
            lista1.listar()

        elif op == "C":
            cargar_datos_prueba(lista1)

        elif op == "3":
            posicion = leer_entero("  Posición: ")
            pasajero = leer_pasajero()
            if lista1.insertar(posicion, pasajero):
                print(" Pasajero insertado")

        elif op == "4":
            cedula = input("  Cédula a buscar: ").strip()
            pos = lista1.buscar(cedula)
            if pos == -1:
                print("   Pasajero no encontrado")
            else:
                print(f"   Encontrado en [{pos}]: {lista1.datos[pos]}")

        elif op == "5":
            print("  ℹ Recuerda ordenar primero (opción 9).")
            cedula = input("  Cédula a buscar (binaria): ").strip()
            pos = lista1.buscar_binaria(cedula)
            if pos == -1:
                print("  Pasajero no encontrado")
            else:
                print(f"   Encontrado en [{pos}]: {lista1.datos[pos]}")

        elif op == "6":
            cedula = input("  Cédula del pasajero a modificar: ").strip()
            nuevo_nombre = input("  Nuevo nombre: ").strip()
            nueva_edad = leer_entero("  Nueva edad: ")
            if lista1.modificar(cedula, nuevo_nombre, nueva_edad):
                print("   Pasajero modificado exitosamente")
            else:
                print("   No se encontró un pasajero con esa cédula")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            quitado = lista1.eliminar_por_posicion(posicion)
            if quitado:
                print(f"   Eliminado: {quitado}")
            else:
                print("   Posición inválida")

        elif op == "8":
            cedula = input("  Cédula del pasajero a eliminar: ").strip()
            if lista1.eliminar_por_valor(cedula):
                print("   Pasajero eliminado por cédula")
            else:
                print("   No se encontró esa cédula")

        elif op == "9":
            lista1.ordenar_asc()
            print("   Lista ordenada ascendentemente:")
            lista1.listar()

        elif op == "10":
            lista1.ordenar_desc()
            print("   Lista ordenada descendentemente:")
            lista1.listar()

        elif op == "11":
            lista1.reversar()
            print("   Lista invertida:")
            lista1.listar()

        elif op == "12":
            copia = lista1.copiar()
            copia.reversar()
            print("\n--- COPIA (reversada) ---")
            copia.listar()
            print("\n--- ORIGINAL ---")
            lista1.listar()

        elif op == "13":
            print(f"   Hay {lista1.longitud()} pasajero(s) en la lista.")

        elif op == "14":
            mayores = lista1.filtrar_mayores_de_edad()
            print("\n--- PASAJEROS MAYORES DE EDAD ---")
            mayores.listar()

        elif op == "15":
            nombres = lista1.nombres_en_mayusculas()
            print(f"   Nombres en mayúsculas: {nombres}")

        elif op == "0":
            break

        else:
            print("  Opción no válida")


# ============================ SUBMENÚ LISTA 2 ========================

def menu_lista2():
    while True:
        mostrar_menu_lista("LISTA 2 · list de Python")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                print("   Pasajero añadido")

        elif op == "2":
            lista2.listar()

        elif op == "C":
            cargar_datos_prueba(lista2)

        elif op == "3":
            posicion = leer_entero("  Posición: ")
            pasajero = leer_pasajero()
            if lista2.insertar(posicion, pasajero):
                print("   Pasajero insertado")

        elif op == "4":
            cedula = input("  Cédula a buscar: ").strip()
            pos = lista2.buscar(cedula)
            if pos == -1:
                print("   Pasajero no encontrado")
            else:
                print(f"   Encontrado en [{pos}]: {lista2.pasajeros[pos]}")

        elif op == "5":
            print("  Recuerda ordenar primero (opción 9).")
            cedula = input("  Cédula a buscar (binaria): ").strip()
            pos = lista2.buscar_binaria(cedula)
            if pos == -1:
                print("   Pasajero no encontrado")
            else:
                print(f"   Encontrado en [{pos}]: {lista2.pasajeros[pos]}")

        elif op == "6":
            cedula = input("  Cédula del pasajero a modificar: ").strip()
            nuevo_nombre = input("  Nuevo nombre: ").strip()
            nueva_edad = leer_entero("  Nueva edad: ")
            if lista2.modificar(cedula, nuevo_nombre, nueva_edad):
                print("   Pasajero modificado exitosamente")
            else:
                print("   No se encontró un pasajero con esa cédula")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            quitado = lista2.eliminar_por_posicion(posicion)
            if quitado:
                print(f"   Eliminado: {quitado}")
            else:
                print("   Posición inválida")

        elif op == "8":
            cedula = input("  Cédula del pasajero a eliminar: ").strip()
            if lista2.eliminar_por_valor(cedula):
                print("   Pasajero eliminado por cédula")
            else:
                print("   No se encontró esa cédula")

        elif op == "9":
            lista2.ordenar_asc()
            print("   Lista ordenada ascendentemente:")
            lista2.listar()

        elif op == "10":
            lista2.ordenar_desc()
            print("   Lista ordenada descendentemente:")
            lista2.listar()

        elif op == "11":
            lista2.reversar()
            print("   Lista invertida:")
            lista2.listar()

        elif op == "12":
            copia = lista2.copiar()
            copia.reversar()
            print("\n--- COPIA (reversada) ---")
            copia.listar()
            print("\n--- ORIGINAL ---")
            lista2.listar()

        elif op == "13":
            print(f"   Hay {lista2.longitud()} pasajero(s) en la lista.")

        elif op == "14":
            mayores = lista2.filtrar_mayores_de_edad()
            print("\n--- PASAJEROS MAYORES DE EDAD ---")
            mayores.listar()

        elif op == "15":
            nombres = lista2.nombres_en_mayusculas()
            print(f"   Nombres en mayúsculas: {nombres}")

        elif op == "0":
            break

        else:
            print("  Opción no válida")


# ============================ MENÚ PRINCIPAL =========================

def main():
    while True:
        print("\n╔══════════════════════════════════╗")
        print("║    TAREA LISTAS · PASAJEROS ✈    ║")
        print("╚══════════════════════════════════╝")
        print("1. Lista 1 (construida desde cero)")
        print("2. Lista 2 (list de Python)")
        print("3. Listar ejercicios")
        print("4. Salir")
        op = input("Opción: ").strip()

        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            menu_ejercicios()
        elif op == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()