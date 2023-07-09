import numpy as np
import random

#Creamos la clase tablero
class Tablero:

    def __init__(self,dimensiones):

#Dimensiones del tablero
        self.dimensiones=dimensiones

#Barcos que se van a colocar en el tablero y su tamaño
        self.barcos=[(1,4), (2, 3), (3, 2), (4, 1)]

#Tablero vacio
        self.tablero=np.full((self.dimensiones,self.dimensiones),' ')

#Creamos el metodo para colocar todos los barcos en el tablero
    def montar_tablero(self):

        for barco in self.barcos:

#Con un bucle while, intentamos colocar los barcos en una posicion valida
            while True:
                fila=random.randint(0,self.dimensiones-1) 
                columna=random.randint(0,self.dimensiones-1)
                orientacion=random.randint(0,1) 

#Si la posicion es valida, colocamos el barco y salimos del bucle. Si no, se genera una nueva posicion
                if self.validar_posicion(fila,columna,barco,orientacion):
                    self.colocar_barco(fila,columna,barco,orientacion)
                    break
 #Creamos el metodo para colocar cada barco con su tamaño y la orientacion que le pasamos             
    def colocar_barco(self,fila,columna,barco,orientacion):
        if orientacion==0:
            for i in range(barco[1]): 
                self.tablero[fila,columna:columna+barco]='O'
        else:
            for i in range(barco[1]):
                self.tablero[fila:fila+barco,columna]='O'

#Creamos el metodo para validar la posicion del barco
    def validar_posicion(self,fila,columna,barco,orientacion):

#Comprobamos que el barco no se salga del tablero y que no se solape con otro barco ya colocado
        if orientacion==0:
            if columna+barco[1]>self.dimensiones:
                return False            
            for i in range(barco[1]):
                if self.tablero[fila,columna+i]!=' ':
                    return False
        else:
            if fila+barco[1]>self.dimensiones:
                return False
            for i in range(barco[1]):
                if self.tablero[fila+i,columna]!=' ':
                    return False
        return True
    



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