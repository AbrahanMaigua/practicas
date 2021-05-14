from collections import deque

turno = deque(["0","X"])
tablero = [
	[" "," "," "],
	[" "," "," "],
	[" "," "," "],
]

def mostra_tablero():
	print ("")
	for fila in tablero:
		print (fila)

def actualizar_tablero(posicion, jugador):
	tablero[posicion[0]][posicion[1]] = jugador

def rotar_turno():
	turno.rotate()
	return turno[0]

def procesar_posicion(posicion):
	fila, columna = posicion.split(",")
	return [int(fila)-1,int(columna)-1]

def posicion_correcta(posicion):
	if 0 <= posicion[0] <= 2 and 0 <=posicion[1] <= 2:
		if tablero[posicion[0]][posicion[1]] == " ":
			return True
	return False
def ha_gando(j):
	# comparas las filas del tablero
	if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
		return True
	# comparas las columnas del tablero
	elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
		return True
	elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
		return True
	elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
		return True
	# comparas las diagonales del tablero
	elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
		return True
	elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
		return True
	
	return False


def juego():
	mostra_tablero()
	jugador = rotar_turno()
	while  True:
		posicion = (input("juega {}, elige la posicion (fila, columna) de 1 a 3. 'salir' para salir ".format(jugador)))
		if posicion == "salir":
			print ("!!!Adios!!!, vuelve pronto.")
			break
		try:
			posicion_1 = procesar_posicion(posicion)
		except:
			print ("Error, posicion {} no validada".format(posicion))
			continue
		if posicion_correcta(posicion_1):
			actualizar_tablero(posicion_1, jugador)
			mostra_tablero()
			if ha_gando(jugador):
				print ("!!!jugador de {} ha ganado!!!".format(jugador))
				break
			jugador = rotar_turno ()

		else:
			print ("posicxion {}, no valida".format(posicion))

juego()