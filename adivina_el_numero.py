'''
logica
1.generar un numero aleatorio
2.registrar el intento en el que se encuentra el jugador
2.crear un bucle
4.si es correto 
	1.mostrar un mensaje de felicitaciones
	2.finalizar el juego 
5.si falla y todavia le quedan intentos
	1.dale una forma de adevinar el numero
	2.mostrar la cantidad de intentos 
	3.incremetar la catidad de intentos
6.si falla y no le quedan intentos
	1.decile a jugador que a finalizado
	2.mostrar el numero 
	3.finalizar la ejecuion
'''
# 1.Generar un numero aleatorio
import random
generador = random.randrange(0,100)
# 2 Regitrar el numero de intentos  
intetntos = 1
# se tiene que iniar en 1 porque si no enpieza a contar desde 0 a 11 como contaria
# un ser humano  
print("""se a generado un numero aleatorio entre 0 a 100
tienes 10 intentos para adivinarlo """)
# 3.crear un bucle 
# 6.si falla y no le quedan intentos	
while intetntos == 10:
	usuario = int(input("\nintroduce un numero: "))
	# 4.si es correto
	if usuario == generador:
		# 1.mostrar un mesaje de felicitaciones
		print(f"felicitaciones\nhas adivinado el numero {generador} \nen la en la cantiada de intetntos {intetntos}" )
		# 2.finalizar la ejecucion
		break
	
	# 5. si falla y todavia le que dadan intentos
	elif usuario >= generador:
		#1.darle al usuario una manera de adivinar el numero
		print("el numero es demaciado alto!")
		#2.mostrale la cantidade de intentos que le quedan
		print("te quedan {} intetntos".format(intetntos))
		#3.incremetar el intento 
		intetntos += 1
	
	# 5. si falla y todavia le que dadan intentos
	elif usuario <= generador:
		# 1.darle al usuario una manera de adivinar el numero
		print("El numero es demaciado bajo!")
		# 2.mostrale la cantidade de intentos que le quedan
		print("te quedan {} intetntos".format(intetntos))
		# 3.incremetar el intento 
		intetntos += 1
# extra		
if intetntos == 10:
	print("\nhas pedido, el numero generado fue ", generador)
		


