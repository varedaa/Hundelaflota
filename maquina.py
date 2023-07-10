import numpy as np
import random
from tablero import Tablero

# Creamos la clase maquina
class Maquina(Tablero):
    def __init__(self, dimensiones, barcos):
        super().__init__(dimensiones, barcos)
        self.tablero_sin_barcos = np.full((self.dimensiones, self.dimensiones), ' ')

    # Creamos el metodo para el turno de la maquina
    def turno_maquina(self, tablero_contrario):
        while True:
            fila = random.randint(0, self.dimensiones - 1)
            columna = random.randint(0, self.dimensiones - 1)
            if tablero_contrario.tablero[fila, columna] == 'O':
                print('La maquina ha acertado')
                tablero_contrario.tablero[fila, columna] = 'X'
            elif tablero_contrario.tablero[fila, columna] == '~' or tablero_contrario.tablero[fila, columna] == 'X':
                print('La maquina ha fallado')
                break
            else:
                print('La maquina ha fallado')
                tablero_contrario.tablero[fila, columna] = '~'
                break

    # Creamos el metodo para comprobar si la maquina ha ganado
    def comprobar_ganador_maquina(self, tablero_contrario):
        if 'O' not in tablero_contrario.tablero:
            print('¡La maquina ha ganado!')
            return False
        else:
            return True

