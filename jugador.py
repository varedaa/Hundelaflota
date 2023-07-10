import numpy as np
import random
from tablero import Tablero

# Creamos la clase jugador
class Jugador(Tablero):
    def __init__(self, dimensiones, barcos):
        super().__init__(dimensiones, barcos)
        self.tablero_sin_barcos = np.full((self.dimensiones, self.dimensiones), ' ')

    # Creamos el metodo para los turnos del jugador
    def turno(self, tablero_contrario):
        while True:
            fila = int(input('Introduce una fila de 0 a 9: '))
            columna = int(input('Introduce una columna de 0 a 9: '))
            if fila < 0 or fila >= self.dimensiones or columna < 0 or columna >= self.dimensiones:
                print('Introduce una posicion valida')
            elif tablero_contrario.tablero[fila, columna] == 'X' or tablero_contrario.tablero[fila, columna] == '~':
                print('Ya has disparado a esa posicion')
                break
            elif tablero_contrario.tablero[fila, columna] == 'O':
                print('Has acertado')
                tablero_contrario.tablero[fila, columna] = 'X'
            else:
                print('Has fallado')
                tablero_contrario.tablero[fila, columna] = '~'
                break

    # Creamos el metodo para comprobar si el jugador ha ganado
    def comprobar_ganador(self, tablero_contrario):
        if 'O' not in tablero_contrario.tablero:
            print('¡Has ganado!')
            return False
        else:
            return True