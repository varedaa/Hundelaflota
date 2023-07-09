import numpy as np
import random
from tablero import Tablero

#Creamos la clase maquina
class Maquina(Tablero):

    def __init__(self,dimensiones):
        self.dimensiones=dimensiones
        self.tablero=np.full((self.dimensiones,self.dimensiones),' ')

#Creamos el metodo para el turno de la maquina
    def turno_maquina(self,tablero_contrario):

#Mientras sea el turno de la maquina, se genera una fila y una columna aleatoria
        while True:
            fila=random.randint(0,self.dimensiones-1)
            columna=random.randint(0,self.dimensiones-1)

#Si  hay un barco, ha acertado y se dispara otra vez
            if tablero_contrario.tablero[fila,columna]=='O':
                print('La maquina ha acertado')
                tablero_contrario.tablero[fila,columna]='X'

#Si la posicion ya ha sido disparada o contiene agua, se indica y se termina el turno           
            elif tablero_contrario.tablero[fila,columna]=='~' or tablero_contrario.tablero[fila,columna]=='X':
                print('La maquina ha fallado')
                break
            else:
                print('La maquina ha fallado')
                tablero_contrario.tablero[fila,columna]='~'
                break

#Creamos el metodo para comprobar si la maquina ha ganado
    def comprobar_ganador_maquina(self,tablero_contrario):

#Si no hay ningun barco en el tablero contrario, la maquina ha ganado
            if np.all(tablero_contrario.tablero=='O')==0:
                print('¡La maquina ha ganado!') 
                return False
            else:
                return True
