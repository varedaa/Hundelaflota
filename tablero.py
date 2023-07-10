import numpy as np
import random
# Creamos la clase tablero
class Tablero:
    def __init__(self, dimensiones, barcos):
        self.dimensiones = dimensiones
        self.barcos = barcos
        self.tablero = np.full((self.dimensiones, self.dimensiones), ' ')

    # Creamos el metodo para colocar todos los barcos en el tablero
    def montar_tablero(self):
        for barco in self.barcos:
            while True:
                fila = random.randint(0, self.dimensiones - 1)
                columna = random.randint(0, self.dimensiones - 1)
                orientacion = random.randint(0, 1)
                if self.validar_posicion(fila, columna, barco, orientacion):
                    if orientacion == 0:
                        for i in range(barco[1]):
                            self.tablero[fila, columna + i] = 'O'
                    else:
                        for i in range(barco[1]):
                            self.tablero[fila + i, columna] = 'O'
                    break

    # Creamos el metodo para validar la posicion del barco
    def validar_posicion(self, fila, columna, barco, orientacion):
        if orientacion == 0:
            if columna + barco[1] > self.dimensiones:
                return False
            for i in range(barco[1]):
                if self.tablero[fila, columna + i] != ' ':
                    return False
        else:
            if fila + barco[1] > self.dimensiones:
                return False
            for i in range(barco[1]):
                if self.tablero[fila + i, columna] != ' ':
                    return False
        return True

 # Creamos el metodo para mostrar el tablero de la maquina con los disparos del jugador, sin mostrar los barcos   
    def mostrar_tablero(self):
        ver_tablero = np.where(self.tablero_sin_barcos == 'O', ' ', self.tablero_sin_barcos)
        disparos = np.where(self.tablero == 'X', 'X', ' ')
        fallos= np.where(self.tablero == '~', '~', ' ')
        tablero_con_disparos = np.where(disparos != ' ', disparos, np.where(fallos != ' ', fallos, ver_tablero))
        print(tablero_con_disparos)

