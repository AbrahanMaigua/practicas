from time import sleep

class ordena:
	def __init__(self):
		self.Pila      = []
		self.Cola      = []
		self.carritos  = []
		self.estateria = []
		# cliente
		self.Cliente  = {} 
		self.name     = ""
		self.apellido = ""
		self.edad     = 0
		self.password = ""
		self.user     = ""

	def cliente(self):
		while True:
			try:
				if len(self.name) == 0:
					self.name     = input("Nombre: ")
					continue
				elif len(self.name) <= 2:
					print("el nombre debe de ser mayor a 3 carrateres")
					self.name     = input("Nombre: ")
					continue
				elif self.apellido == "":
					self.apellido = input("Apellido: ")
					continue
				
				elif self.edad == 0:
					self.edad     = int(input("Edad: "))
					continue

				elif self.edad <= 17:
					print("edad no valida")
					self.edad     = int(input("Edad: "))
					continue	
				elif self.user == "" or None:
					self.user     = input("usuario: ")
				elif self.password == "" or None:	
					self.password = input("password: ")
					continue
				elif self.Cliente == {}:
					self.Cliente = self.user, self.password

					print("\nse a realizado el regitro satifatoriamente!!!")
					print(f"Bienbenido/a {self.name} {self.apellido}\n" )
					sleep(5)
					break 
			except ValueError:
				global carrateresNoValido
				print("solo lo se permiten numeros")


	def mayor_menor(self, entrada):
		run = 2
		b = int(max(entrada)) 
		auxiliar = []
		auxiliar.append(b)
		while run < len(entrada):
			for indix_put in entrada:
				if auxiliar[0] > indix_put:
					if (b - indix_put) == 1:
						b -= 1
						run += 1
						self.put.insert(0, indix_put )
		return (self.put)
	
	def pila(self, size, add):
		cola = []
		for index in add:
			print(len(cola))
			if len(cola) >= size:
				print ("etamos llenos.")
				break
			else:
				cola.append(index)
				self.Pila.append(index)
		

	def sacar(self,nun=int):
		if nun == 1:
			try:			
				self.Pila.pop(0) # primero que entra sale
				return True

			except IndexError:
				return False
				print ("pila vacia")

		elif nun == 2:
			try:
				self.Cola.remove(self.Cola[-1])
				return True
						
			except IndexError:
				return False
				print ("cola vacia")
		else:
			return False

	def cola(self, add):
		if type(add) == str or int or float or bool or bytes:
			self.Cola.insert(-1 ,add)
			#self.Cola.append()
			#self.insert
		else:
			for cliente in add:
				self.Cola.insert(-1, cliente)

persona = ["kaiju no 8","abrahan","mark","apele"]
ic = 0
while True:
	print("bienvenido a SIGO.\n".capitalize())
	tienda  = ordena() 
	opcione = ["registro","iniciar secion",
			  "Tomar carrito de compra","Buscar articulo","Pagar"]
	for i in opcione:
		if len(opcione) > ic:
			ic += 1
		elif ic == len(opcione):
			ic -= ic 
			ic += 1
		print(f"{ic}.", i)

	try:		
		user = int(input("\nque desas realizar el dia de hoy?\n\n"))
		
		if opcione[user-1] == opcione[0]:
			print(f"\n{opcione[user-1]}\n")
			clinte_Nuevo = tienda.cliente()
			if clinte_Nuevo == ValueError:
				raise ValueError
				clinte_Nuevo = tienda.cliente()

		elif opcione[user-1] == opcione[1]:
			print(f"{opcione[user-1]}")
			
		elif opcione[user-1] == opcione[2]:
			print(f"{opcione[user-1]}")
			break

		elif opcione[user-1] == opcione[3]:
			print(f"{opcione[user-1]}")
			break
		elif opcione[user-1] == opcione[4]:
			print(f"{opcione[user-1]}")
			break
		elif opcione[user-1] == opcione[5]:
			print(f"{opcione[user-1]}")
			break	
			
		#else:
		#	print (f"la opcion {user} no es vlida")	
			

	except IndexError as e:
		print (f"opcion {user} no valida por favor introduca una opcion valida")
	except ValueError as carrateresNoValido:
		print("solo se admiten carrateres numericos")
	except KeyboardInterrupt:
			print ("Hasta luego gracias, por visitarnos!!!")
			break	
	
	