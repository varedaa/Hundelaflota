import numpy as np
import random
from tablero import Tablero
from maquina import Maquina
from jugador import Jugador

dimensiones=10
barcos = [(1, 4), (2, 3), (3, 2), (4, 1)]
tablero_jugador=Jugador(dimensiones,barcos)
tablero_maquina=Maquina(dimensiones,barcos)

#Creamos el metodo para colocar los barcos
tablero_jugador.montar_tablero()
tablero_maquina.montar_tablero()

#Empiezan los turnos
while True:
    print('¡Es tu turno!')
    #Jugador.mostrar_tablero(Maquina)
    tablero_jugador.turno(Maquina)
   
    if Jugador.comprobar_ganador(Maquina)==False:
        break
    print('¡Turno de la maquina!')
    tablero_maquina.turno(Maquina)
    
    if Maquina.comprobar_ganador_maquina(Jugador)==False: 
        
        break


"""if np.all(tablero_contrario.tablero=='O')==0:
                print('¡Has ganado!') 
                return False
elif np.all(tablero.tablero=='O')==0:
                print('¡Ha ganado la maquina!') 
                return False
            else:
                return True"""
""""""