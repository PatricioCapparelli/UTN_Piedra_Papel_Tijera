import random

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    '''Funcion que recibe dos parametros numericos que son los valores del juego, si uno vence al otro devuelve el ganador de la ronda y si los dos tienen el mismo elemento devuelve empate.
        Args:
            jugador (int): Numero del jugador.
            maquina (int): Numero de la maquina.

        Returns:
            str: Devuelve el ganador del juego o el empate. "Jugador", "Maquina", "Empate".
    '''
    ganador = None

    if jugador == maquina:
        ganador = "Empate"
    elif jugador == 1 and maquina == 3:
        ganador = "Jugador"
    elif jugador == 2 and maquina == 1:
        ganador = "Jugador"
    elif jugador == 3 and maquina == 2:
        ganador = "Jugador"
    elif maquina == 1 and jugador == 3:
        ganador = "Maquina"
    elif maquina == 2 and jugador == 1:
        ganador = "Maquina"
    elif maquina == 3 and jugador == 2:
        ganador = "Maquina"
    
    return ganador
    
def validar_numero(cadena: str) -> bool:
    '''Funcion que recibe una cadena y verifica si es numerica, o en caso de error que hallan otros tipos de datos.
        Args:
            cadena (str): Cadena a verificar.

        Returns:
            bool: Devuelve el booleano, si el dato es valido devuelve True, si es invalido False.
    '''
    if len(cadena) != 1:
        return False  
    if ord(cadena) >= 49 and ord(cadena) <= 51:
        return True
    return False

def validar_cadena(cadena: str) -> bool:
    '''Funcion que recibe una cadena y verifica si sus datos son validos.
        Args:
            cadena (str): Cadena a verificar.

        Returns:
            bool: Devuelve el booleano, si el dato es valido devuelve True, si es invalido False.
    '''
    flag = True
    if cadena != "si" and cadena != "no":
        return False
    return flag

def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    '''Funcion que recibe tres parametros y verifica el estado de la partida, si hay dos aciertos del jugador o la maquina devuelve False y ademas si la ronda es la 3 tambien. Sino sigue el juego. 
        Args:
            aciertos_jugador (int): Numero de aciertos del jugador.
            aciertos_maquina (int): Numero de aciertos de la maquina.
            ronda_actual (int): Numero de rondas.

        Returns:
            bool: Devuelve el booleano, si se completaron el maximo de aciertos o rondas.
    '''
    partida = True
    if aciertos_jugador == 2 or aciertos_maquina == 2 or ronda_actual >= 3:
        partida = False
    return partida

def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    '''Funcion que recibe dos parametros y verifica el ganador de la partida, devuelve el que tenga mas aciertos entre el jugador o la maquina y si tienen la misma cantidad devuelve empate. 
        Args:
            aciertos_jugador (int): Numero de aciertos del jugador.
            aciertos_maquina (int): Numero de aciertos de la maquina.

        Returns:
            str: Devuelve la cadena del jugador, maquina o empate.
    '''
    ganador = None
    if aciertos_jugador == aciertos_maquina:
        ganador = "Empate"
    elif aciertos_maquina > aciertos_jugador:
        ganador = "Maquina"
    elif aciertos_jugador > aciertos_maquina:
        ganador = "Jugador"
    return ganador

def mostrar_elemento(eleccion: int) -> str:
    '''Funcion que recibe el elemento seleccionado por el jugador o la maquina y lo devuelve en forma de cadena.  
        Args:
            eleccion (int): Numero del elemento.

        Returns:
            str: Devuelve la cadena del elemento Piedra, Papel, o Tijera.
    '''
    elemento = None
    if eleccion == 1:
        elemento = "Piedra"
    if eleccion == 2:
        elemento = "Papel"
    if eleccion == 3:
        elemento = "Tijera"
    return elemento

def pedir_eleccion_jugador() -> int:
    '''Funcion que pide al jugador que elija una opcion numerica.  
        Args:
            None:

        Returns:
            int: devuelve el entero de la opcion elegida, 1, 2, 3.
    '''
    while True:
        eleccion = input("Elige una opcion numerica (1 Piedra), (2 Papel), (3 Tijera): ")
        if validar_numero(eleccion):
            return int(eleccion)
        else:
            print("Entrada invalida. Debe ser 1, 2 o 3.")

def jugar_piedra_papel_tijera() -> str:
    '''Funcion que inicia una partida donde el jugador compite contra la maquina.
    En cada ronda, el jugador elige una opcion y la maquina genera una eleccion aleatoria.
    Se determina el ganador de la ronda.
    Se verifica si la partida continua o si alguien ha ganado.
    Al finalizar, la funcion devuelve quien gano la partida ("Jugador" o "Maquina" o "Empate")
        Args:
            None:

        Returns:
            str: Devuelve el ganador del juego o el empate.
    '''
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0
    juego_activo = True

    print("Comienza la partida: Piedra, Papel o Tijera (mejor de 3)")
    
    while juego_activo:
        print(f"\nRonda {ronda_actual + 1}")
        jugador = pedir_eleccion_jugador()
        maquina = random.randint(1, 3)

        print(f"Jugador eligio: {mostrar_elemento(jugador)}")
        print(f"Maquina eligio: {mostrar_elemento(maquina)}")

        ganador_ronda = verificar_ganador_ronda(jugador, maquina)
        print(f"Resultado de la ronda: {ganador_ronda}")

        if ganador_ronda == "Jugador":
            aciertos_jugador += 1
        elif ganador_ronda == "Maquina":
            aciertos_maquina += 1

        ronda_actual += 1

        
        if verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) == False:
            ganador_partida = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
            print(f"\nFin del juego! El ganador de la partida es: {ganador_partida}")
            
            
            if ganador_partida == "Empate":
                opcion = input("EMPATE!!! Desea seguir jugando? (si/no): ")
                while validar_cadena(opcion) == False:
                    opcion = input("Error: elija una opcion en minuscula (si/no): ")
                
                if opcion == "si":
                    aciertos_jugador = 0
                    aciertos_maquina = 0
                    ronda_actual = 0
                else:
                    juego_activo = False
            else:
                opcion = input("Desea jugar otra partida? (si/no): ")
                while validar_cadena(opcion) == False:
                    opcion = input("Error: elija una opcion en minuscula (si/no): ")
                
                if opcion == "si":
                    
                    aciertos_jugador = 0
                    aciertos_maquina = 0
                    ronda_actual = 0
                else:
                    juego_activo = False
    
    return ganador_partida

jugar_piedra_papel_tijera()