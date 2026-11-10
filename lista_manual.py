# =====================================================================
#  lista_manual.py  —  LISTA 1: construida DESDE CERO (como MiLista)
# ---------------------------------------------------------------------
#  Esta clase imita la clase MiLista del módulo 7 de la guía.
#  Por dentro hay un ARREGLO de tamaño fijo con cajones vacíos (None).
#
#      datos     -> [Ana, Beto, Carlos, None, None, ...]
#      capacidad -> cuántos cajones hay en total          (10)
#      cantidad  -> cuántos cajones están ocupados        (3)
#
#  LAS DOS REGLAS QUE EXPLICAN TODA LA CLASE
#    1. Los pasajeros van SEGUIDOS: de datos[0] a datos[cantidad-1].
#       No puede haber huecos (None) en medio.
#    2. Para INSERTAR se corre a la DERECHA (de atrás hacia adelante).
#       Para ELIMINAR se corre a la IZQUIERDA (de adelante hacia atrás).
#
#  ⛔ PROHIBIDO en esta clase (aquí se trabaja "a mano"):
#     append, insert, pop, remove, index, sort, sorted, reverse,
#     reversed, copy, len(), el operador "x in lista" para buscar,
#     slicing [a:b] ni comprensiones.  (for i in range(...) SÍ se puede)
#  ✅ PERMITIDO: índices datos[i], while, for i in range(...), if,
#     variables auxiliares (aux), y self.cantidad / self.capacidad.
#
#  📌 Método de trabajo para CADA método (el método de 5 pasos):
#     1) Entrada / Proceso / Salida   2) Bosquejo a mano con datos
#     3) Descubrir el patrón          4) Escribir el código
#     5) Prueba de escritorio
#
#  Cuando termines un método, BORRA la línea "pass".
# =====================================================================

from pasajero import Pasajero


class ListaPasajerosManual:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad   # los "cajones"
        self.capacidad = capacidad        # cuántos cajones hay
        self.cantidad = 0                 # cuántos están ocupados

    # -----------------------------------------------------------------
    # 1. AÑADIR  ✅ YA RESUELTO (úsalo como modelo)
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Pone el pasajero en el primer cajón libre (al final)."""
        if self.cantidad == self.capacidad:
            print("⚠ La lista está llena")
            return False
        # El primer cajón libre SIEMPRE es datos[cantidad]
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True
        # 🔧 MEJORA cuando termines buscar(): antes de añadir, verifica
        #    que la cédula no exista:  if self.buscar(pasajero.cedula) != -1

    # -----------------------------------------------------------------
    # 2. LISTAR  ✅ YA RESUELTO (úsalo como modelo)
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición."""
        if self.cantidad == 0:
            print("(lista vacía)")
            return
        for i in range(self.cantidad):          # solo los cajones ocupados
            print(f"[{i}] {self.datos[i]}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        return self.cantidad

    # -----------------------------------------------------------------
    # 4. INSERTAR EN UNA POSICIÓN
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        if self.cantidad >= self.capacidad:
            print("La lista esta llena")
            return False

        if posicion < 0 or posicion > self.cantidad:
            print("Posicion no valida")
            return False

        i= self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i-1]
            i= i-1

        self.datos[posicion]= pasajero
        self.cantidad += 1
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR (LINEAL) POR CÉDULA
    # -----------------------------------------------------------------
    def buscar(self, cedula):

        for i in range(self.cantidad):
            if self.datos[i].cedula==cedula:
                return i
        return -1
       

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA POR CÉDULA
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):

        izq= 0
        der=self.cantidad -1
        while izq <= der:
            medio = (izq + der)// 2
            if self.datos[medio].cedula == cedula:
                return medio
            if self.datos[medio].cedula < cedula:
                izq= medio +1
            else:
                der = medio -1
        return -1
        

    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):

        pos= self.buscar(cedula)
        if pos== -1:
            print("no existe")
            return False
        self.datos[pos].nombre = nuevo_nombre
        self.datos[pos].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):

        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None
        valor = self.datos[posicion]
        for i in range(posicion, self.cantidad -1):
            self.datos[i] = self.datos[i +1]
        self.datos[self.cantidad - 1]= None
        self.cantidad  -=1
        return valor
 
    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)
    # -----------------------------------------------------------------

    def eliminar_por_valor(self, cedula):

        pos = self.buscar(cedula)
        if pos == -1:
            print("Posicion no valida")
            return False
        self.eliminar_por_posicion(pos)
        return True

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula) — MÉTODO BURBUJA
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n -1):
            for i in range(n -1 - vuelta):
                if self.datos[i].cedula > self.datos[i+1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[ i +1]
                    self.datos[ i +1] = aux


    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
          n = self.cantidad
          for vuelta in range(n -1):
                    for i in range(n -1 - vuelta):
                        if self.datos[i].cedula < self.datos[i+1].cedula:
                            aux = self.datos[i]
                            self.datos[i] = self.datos[ i +1]
                            self.datos[ i +1] = aux
        


    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        izq=0 
        der=self.cantidad -1
        while izq < der:
            aux= self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der]= aux
          
            izq +=1
            der -=1
      

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        nueva= ListaPasajerosManual(self.capacidad)
        for i in range (self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva


    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD (versión manual de una "comprensión")
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):

        resultado= ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            if self.datos[i].es_mayor_de_edad(): resultado.añadir(self.datos[i])
        return resultado

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS (versión manual de una "comprensión")
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):

        resultado = [None] * self.cantidad
        for i in range(self.cantidad):
            resultado[i] = self.datos[i].nombre.upper()
        return resultado
     
