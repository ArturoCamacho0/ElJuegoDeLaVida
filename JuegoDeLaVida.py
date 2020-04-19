import pygame
import numpy as np
import time

# Creando la pantalla para visualizar el juego
pygame.init()
ancho, alto = 600, 600
pantalla = pygame.display.set_mode((ancho, alto))
bg = 25, 25, 25
pantalla.fill(bg)


# Creando las celdas
# Número de celdas a crear
nxC, nyC = 50, 50

# Tamaño de las celdas
dimCW = ancho / nxC
dimCH = alto / nyC

#Estado de las celdas. Si es 1 está viva; si es 2 está muerta.
estadoJuego = np.zeros((nxC, nyC))

# Automata palo
# estadoJuego[5, 3] = 1
# estadoJuego[5, 4] = 1
# estadoJuego[5, 5] = 1

# Automata movil
estadoJuego[21, 21] = 1
estadoJuego[22, 22] = 1
estadoJuego[22, 23] = 1
estadoJuego[21, 23] = 1
estadoJuego[20, 23] = 1


# Control para pausar el juego
pausar = False

# Ejecucion para mostrar las celdas y la pantalla
while True:

	# Reiniciar los estados de las celdas
	nuevoEstadoJuego = np.copy(estadoJuego)

	# Reiniciar el fondo de la pantalla
	pantalla.fill(bg)
	time.sleep(0.1)

	# Registro de eventos con el teclado o el ratón
	ev = pygame.event.get()

	for event in ev:
		# Se detecta si se presionó una tecla
		if event.type == pygame.KEYDOWN:
			pausar = not pausar

		# Se detecta si se presionó el mouse
		clickMouse = pygame.mouse.get_pressed()

		if sum(clickMouse) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			nuevoEstadoJuego[celX, celY] = not clickMouse[2]

	for y in range(0, nxC):
	  	for x in range(0, nyC):

	  		if not pausar:
		  		# Algoritmo de vecinos cercanos
		  		n_vecino = estadoJuego[(x - 1) % nxC, (y - 1) % nyC] + \
		  				   estadoJuego[(x)     % nxC, (y - 1) % nyC] + \
		  				   estadoJuego[(x + 1) % nxC, (y - 1) % nyC] + \
		  				   estadoJuego[(x - 1) % nxC, (y)     % nyC] + \
		  				   estadoJuego[(x + 1) % nxC, (y)     % nyC] + \
		  				   estadoJuego[(x - 1) % nxC, (y + 1) % nyC] + \
		  				   estadoJuego[(x)     % nxC, (y + 1) % nyC] + \
		  				   estadoJuego[(x + 1) % nxC, (y + 1) % nyC]

		  		# Regla #1: Una célula muerta con exactamente 3 vecinas vivas, "revive"
		  		if estadoJuego[x, y] == 0 and n_vecino == 3:
		  			nuevoEstadoJuego[x, y] = 1


		  		# Regla #2: Una célula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
		  		if estadoJuego[x, y] == 1 and (n_vecino > 3 or n_vecino < 2):
		  			nuevoEstadoJuego[x, y] = 0

	  		# Creamos el poligono con las celdas
	  		poligono = [((x) *     dimCW,  y      * dimCH),
	  					((x + 1) * dimCW,  y      * dimCH),
	  					((x + 1) * dimCW, (y + 1) * dimCH),
	  					((x)     * dimCW, (y + 1) * dimCH),]

	  		# Dibujamos el poligono en la pantalla
	  		if nuevoEstadoJuego[x, y] == 0:
	  			pygame.draw.polygon(pantalla, (128, 128, 128), poligono, 1)
	  		else:
	  			pygame.draw.polygon(pantalla, (255, 255, 255), poligono, 0)

	# Actualizar el estado del juego
	estadoJuego = np.copy(nuevoEstadoJuego)

	# Mostramos la ejecución
	pygame.display.flip()

	if event.type == pygame.QUIT:
            # detiene el bucle
            break

# finaliza Pygame
pygame.quit()