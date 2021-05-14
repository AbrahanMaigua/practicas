import cv2 
import numpy as np 
import imutils 

# detetamos los colores
def color(img):
	color_bajo1 = np.array([0 , 0  , 19 ], np.uint8)
	color_alto1 = np.array([0, 255, 255], np.uint8)
	color_bajo2 = np.array([135, 0  ,90], np.uint8)
	color_alto2 = np.array([180, 255, 255] ,np.uint8)


	lista = [] 
	#img   = cv2.imread('images.jpg')
	img    = cv2.imread(img) 
	size_0 = imutils.resize(img, width=640)
	
	# converciones 
	gray  =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # de BGR  a GRAY
	gray  =cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # de GRAY a BGR
	HVS   =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # de BGR  a HSV
	
	# detetecion de color 
	maskColor1 = cv2.inRange(HVS,color_bajo1,color_alto1 )
	maskColor2 = cv2.inRange(HVS,color_bajo2,color_alto2 )
	mask       = cv2.add(maskColor1, maskColor2)
	mask 	   = cv2.medianBlur(mask, 7) 
	colDetected= cv2.bitwise_and(img,img, mask=mask) 	  # para visulizar el color que quremos detectar 
	
	# fondo a escala de gris
	
	invMask = cv2.bitwise_not(mask) 					# invertimos la mask en para convertir los espasios positivos en negtivos y viseversa
	bgGray  = cv2.bitwise_and(gray,gray , mask=invMask) # para visulizar la imagen en escala de grises 

	# sumamos la imagenes 

	output = cv2.add(bgGray, colDetected)
	size_2 = imutils.resize(output, width=640)

	size_1 = cv2.resize(mask, (550,550),)

	# visualizamos la imagen 

	cv2.imshow('output', size_2)
	

	#salida = open("salida.jpg", "w+")
	#salida.write(output)
    #salida.close()
	cv2.waitKey(0)
	cv2.destroyAllWindows()

