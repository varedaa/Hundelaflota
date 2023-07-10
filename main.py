import numpy as np
import random
from tablero import Tablero
from maquina import Maquina
from jugador import Jugador

dimensiones = 10
barcos = [(1, 4), (2, 3), (3, 2), (4, 1)]
tablero_jugador = Jugador(dimensiones, barcos)
tablero_maquina = Maquina(dimensiones, barcos)

# Creamos el metodo para colocar los barcos
tablero_jugador.montar_tablero()
tablero_maquina.montar_tablero()


#Empieza el juego 
print('''   ¡Bienvenido/a a Hundir la flota!
En este juego deberas hundir todos los barcos de la maquina antes de que ella hunda los tuyos.
Elige fila y columna a la que disparar, si aciertas, se marcará con una X y podrás volver a disparar.
Si fallas, se marcará con una ~ y será el turno de la maquina.
¡Buena suerte!''')

# Empiezan los turnos.
while True:

#Se muestra el tablero al que se le va a disparar y se hace turno hasta que falle
    print('¡Es tu turno!')
    tablero_maquina.mostrar_tablero()
    tablero_jugador.turno(tablero_maquina)

#Se comprueba si el jugador ha ganado. Si no, continua el juego
    if tablero_jugador.comprobar_ganador(tablero_maquina) == False:
        break

#Cuando el jugador falla, es el turno de la maquina. Continua hasta que falle
    print('¡Turno de la maquina!')
    tablero_maquina.turno_maquina(tablero_jugador)

#Se comprueba si la maquina ha ganado. Si no, continua el juego
    if tablero_maquina.comprobar_ganador_maquina(tablero_jugador) == False:
        break