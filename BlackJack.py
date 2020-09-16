import random

#Función para añadir cartas a la baraja:
#"palo", es un caracter unicode. (corazón, pica, trebol, diamante)
#"números", es el vector de posibilidades para el palo.

#La función añade una carta por cada "número" en el vector "numeros", combinando además el caracter del número con el caracter del palo. 
#ej: (2♥️)
def BarajarPalo(baraja, palo, numeros):
    if(len(numeros) == 0): 
        return baraja
    
    baraja.append(numeros.pop() + palo)
    return BarajarPalo(baraja, palo, numeros)      


#Función para barajar las cartas:
#"baraja", es el vector donde se acumulan los resultados de la adición de cada palo.

#La función resuleve el caracter unicode asociado a cada palo e invoca la función "BarajarPalo", al final revuelve la baraja.
def Barajar(baraja):  
    BarajarPalo(baraja, '\u2660', {'2', '3', '4', '5','6','7','8','9','10','A','J','Q','K'})
    BarajarPalo(baraja, '\u2661', {'2', '3', '4', '5','6','7','8','9','10','A','J','Q','K'})
    BarajarPalo(baraja, '\u2662', {'2', '3', '4', '5','6','7','8','9','10','A','J','Q','K'})
    BarajarPalo(baraja, '\u2663', {'2', '3', '4', '5','6','7','8','9','10','A','J','Q','K'})
  
    #revuelve aleatoriamente la baraja.
    random.shuffle(baraja)    
    return baraja


#Función para extraer Carta:
#"baraja", es el vector que contiene todas las cartas.
#"jugador", es el vector de cartas propio del jugador.

#La función asigna una carta del principio de la baraja al "jugador" extrañendola de la "baraja".
def DarCarta(baraja, jugador):
    jugador.append(baraja.pop())   
    return jugador[-1]


#Función para calcular el total:
#"mano", es el vector de cartas propio del jugador.
#"valores", es un diccionario con el valor numérico de cada carta.
#"resultado", es la variable numérica donde se apila el resultado del total.

#La función acumula en "resultado", el valor numérico de cada carta, conforme a la busqueda en "valores".
#También controla la doble función del "As".
def CalcularTotal(mano, valores, resultado):
    if(len(mano) == 0): return resultado

    #Si la carta que se está totalizando es un As, y el acumulado es mayor que 21, se asume el As como 1 y no como 11.
    if mano[0][0] == "A" and resultado + valores[mano[0][0]] > 21:
        return CalcularTotal(mano[1:], valores, resultado + 1)

    return CalcularTotal(mano[1:], valores, resultado + valores[mano[0][0]])


#Funcion totalizadora de mano:
#"mano", es el vector de cartas propia del jugador.

#La función invoca a otra función llamada "CalcularTotal", 
#resolviendo el parametro del diccionario, con el valor numérico de cada carta posible.
def Total(mano):
    return CalcularTotal(mano, {'2':2, '3':3, '4':4, '5':5,'6':6,'7':7,'8':8,'9':9,'1':10,'A':11,'J':10,'Q':10,'K':10}, 0)


#Función Compara Manos
#"casa", es el vector de cartas propio de la casa (computador).
#"jugador", es el vector de cartas propio del jugador.

#La función compara los totales por mano en caso de empate gana la casa, en caso de que ambos tengan 21,
#y si alguno hizo 21 con dos cartas, ese es el ganador en otro caso gana la casa.
def CompararManos(casa, jugador):
    if Total(jugador) > 21:
        print("¡Perdiste!")
    elif Total(casa) > 21:
        print("¡Ganaste!")
    elif Total(casa) > Total(jugador):
        print("¡Perdiste!")
    elif Total(casa) < Total(jugador):
        print("¡Ganaste!")
    elif Total(casa) == 21 and 2 == len(casa) < len(jugador):
        print("¡Perdiste!")
    elif Total(jugador) == 21 and 2 == len(jugador) < len(casa):
        print("¡Ganaste!")
    elif Total(jugador) == Total(casa):
        print("¡Perdiste!")
    else :
        print ("Empate")


#Función que encapsula el turno de un jugador
#"nombreJugador", es el nombre que el usuario digitó en pantalla.
#"baraja", es el vector que contiene todas las cartas.
#"mano", es el vector de cartas propio del jugador.

#La función pregunta por la extracción de una carta, en caso afirmativo 
#extrae una carta, la muestra al usuario, la totaliza y vuelve apreguntar. 
#En caso de sumar mas de 21, se finaliza el turno sin preguntar.
def Turno(nombreJugador, baraja, mano):
    
    if input("¿Otra Carta (Si o No)? (Enter significa si) :") in ("no", "N", "n", "NO", "No", "nO"):
        print("Fin del turno del jugador: {:>7}".format(nombreJugador))
        print("-----")
        return

    print("Tu carta: {:>7}".format(DarCarta(baraja, mano)))
    print("Total: {:>7}".format(Total(mano)))
    
    if Total(mano) > 21:
        print("Te pasaste!")
        print("-----")
        return
    
    return Turno(nombreJugador, baraja,mano)


#Función de Inicio/Control de cada partida:
#"nombreJugador", es el nombre que el usuario digito en pantalla.
#"baraja", es el vector que contiene todas las cartas.
#"casa", es el vector de cartas propio de la casa (computador).
#"jugador", es el vector de cartas propio del jugador.

#La función realiza la asignación de dos cartas a cada jugador, 
#luego invoca la función "Turno", despues de esto, y dado que no se haya pasado (obtenido mas de 21),
#se simula el juego de la casa. Al final, se comparan las manos para conocer el ganador.
def Ventiuna(nombreJugador, baraja, casa, jugador):
    for entero in range(2):
        DarCarta(baraja,jugador)
        DarCarta(baraja,casa)
    
    print("La Casa: {:>7}   *".format(casa[0], casa[1]))
    print("{:>7}: {:>7}{:>7}".format(nombreJugador, jugador[0], jugador[1]))

    Turno(baraja,jugador,nombreJugador)

    if(Total(jugador) <= 21):
        while Total(casa) < 17:           
            print ("La Casa obtuvo {:>7}".format(DarCarta(baraja,casa)))
            print("total: {:>7}".format(Total(casa)))

            if Total(casa) > 21:
                print("La Casa se paso")   
                print("-----")             

    CompararManos(casa,jugador)
    print("-----")
    print("Manos Finales: ")
    print("La Casa, Total {:>7}".format(Total(casa)))
    print(casa)
    print(nombreJugador + ", Total {:>7}".format(Total(jugador)))
    print(jugador)
    print("-----")
    return


#Función Control de cada juego:
#"respuesta", es el control de inicio de otra partida.
#"nombreJugador", es el nombre que el usuario digito en pantalla.

#La función invoca el control de cada partida. al finalizar pregunta al usuario para iniciar o no otra partida.
def Juego(respuesta, nombreJugador):    
    if(respuesta in ("no", "N", "n", "NO", "No", "nO")):
        print("Fin del juego")
        return

    print("Inicia de Nuevo Juego:")

    Ventiuna(nombreJugador, Barajar([]),[],[])

    return Juego(input("¿Otra Partida? Si o No: (Enter significa si) "), nombreJugador)


#Linea que inicia la ejecución de la aplicación.
Juego("inicio", input("Bienvenido, ingrese su nombre: "))