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
    