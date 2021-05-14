# importaciones
import os  # simtema
import time  # tiempo
import calendar  # calendario


def caja():
    total = 10
    lista = []
    salir = True
    while (salir):
        localtime = time.localtime()
        print(time.asctime(localtime))
        print('Biemvenido, a este programa.\n')
        #opcion = input('introcuce un numero:')
        opcion = '2'
        os.system('clear')
        if opcion == "1":
            objectos = 0
            objectos = int(input('introcuce la cantidad de objetos: '))
            print('total de productos:', objectos)

            time.sleep(3)
            os.system('clear')

        elif opcion == '2':
            print('total de productos:',total)
            for i in range(total):
                nombre_producto = (input('nombre_producto:%s.' % i))
                lista = nombre_producto[i]
            time.sleep(3)
        	os.system('clear') # error en esta linia
        	


        elif opcion == '3':
        	print (lista)
        	time.sleep(3)
        	os.system('clear')




caja()
