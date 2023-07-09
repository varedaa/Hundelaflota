import numpy as np
import random
from tablero import Tablero


#Creamos la clase jugador
class Jugador(Tablero):
    
    def __init__(self,dimensiones):
        self.dimensiones=dimensiones
        self.tablero=np.full((self.dimensiones,self.dimensiones),' ')

#Creamos el metodo para los turnos del jugador   
    def turno(self,tablero_contrario):

#Mientras sea el turno del jugador, se le pide que introduzca una fila y una columna
        while True:
            fila=int(input('Introduce una fila de 0 a 9: '))
            columna=int(input('Introduce una columna de 0 a 9: '))

 #Si la posicion no es valida, se pide que introduzca otra posicion       
            if fila<0 or fila>=self.dimensiones or columna<0 or columna>=self.dimensiones:
                print('Introduce una posicion valida')

 #Si la posicion es valida pero ya ha sido disparada, se indica y se termina el turno          
            elif tablero_contrario.tablero[fila,columna]=='X' or tablero_contrario.tablero[fila,columna]=='~':
                print('Ya has disparado a esa posicion')
                break

#Si la posicion es valida y hay un barco, ha acertado y se dispara otra vez
            elif tablero_contrario.tablero[fila,columna]=='O':
                print('Has acertado')
                tablero_contrario.tablero[fila,columna]='X'

#Si la posicion es valida y no hay un barco, se le indica que ha fallado y se cambia el turno a la maquina
            else:
                print('Has fallado')
                tablero_contrario.tablero[fila,columna]='~'
                break            

#Creamos el metodo para comprobar si el jugador ha ganado
    def comprobar_ganador(self,tablero_contrario):
#Si no hay ningun barco en el tablero contrario, el jugador ha ganado
            if np.all(tablero_contrario.tablero=='O')==0:
                print('¡Has ganado!') 
                return False
            else:
                return True