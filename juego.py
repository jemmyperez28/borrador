import os
'''
Version 1.0 Por Fermin.
Agreguen sus ideas con push al repo : 
https://github.com/jemmyperez28/borrador
chony se la come.
'''

#Variables , cartas , etc.
turno="jugador1"
fase="seteo"
jugador1_hp=1000
jugador2_hp=2000

                    
while True:  
    #Primera Fase Player 1 inicia
    if turno=="jugador1" and fase=="seteo" :
        print("Fase Seteo player 1")
        print("Elija Opciones")
        print("1.Invocar Monstruo")
        print("2.Invocar carta trampa")
        eleccion1 = int(input("Ingrese Opcion:")) 
        if eleccion1 == 1:
            os.system('clear')
            print("Se ha invocado un monstruo")
            monstruo1_hp=100
            print("Vida monstruo :" + str(monstruo1_hp))
            #Pasar a la siguiente Fase
            fase=="ataque"
            pass
        if turno=="jugador1" and fase=="ataque":
            print("Fase Ataque player 1")
            print("Elija Opciones")
            print("1.Atacar")
            eleccion2 = int(input("Ingrese Opcion:")) 