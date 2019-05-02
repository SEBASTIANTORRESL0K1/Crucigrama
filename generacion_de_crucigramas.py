''' En este Módulo se generan los crucigramas finales, y se le da a la impresión en pantalla el formato correcto:
. Se generan dos crucigramas, uno codificado y otro con soluciones
. Se agregan los indicadores (se agregan directamente dentro de la Matriz, entonces el método se utiliza dentro de la sección armado_de_matriz)
. Se imprimen las definiciones de las palabras seleccionadas
. Se determina si se incluye o no el crucigrama con las soluciones
'''

import argparse

def generar_crucigramas(matriz):
	''' Recibe una Matriz
		Devuelve dos cadenas que emulan dos crucigramas (uno con soluciones y otro codificado) a partir de esa Matriz
	'''
	matriz_soluciones = []
	matriz_codificada = []
	for fila in matriz:
		fila_soluciones = ''
		fila_codificada = ''
		for j,letra in enumerate(fila):
			if letra == ' ':
				fila_soluciones += letra * 2
				fila_codificada += letra * 2
			else:
				fila_soluciones += letra+' '
				if j != 1 and letra.isalpha(): # Me aseguro de no codificar los indicadores del crucigrama
					fila_codificada += '. '
				else:
					fila_codificada += letra+' '			
		matriz_soluciones.append(fila_soluciones)
		matriz_codificada.append(fila_codificada)
	return matriz_soluciones,matriz_codificada

def agregar_indicadores(matriz,horizontal,fila_de_horizontal,verticales,informacion_de_verticales):
	''' Recibe una Matriz, una palabra horizontal, su fila en la Matriz, una lista de palabras verticales y un diccionario con información sobre las mismas
		Devuelve una Matriz similar a la primera, pero agrega filas y columnas con datos que eventualmente servirán como información para el usuario
	'''
	for i,fila in enumerate(matriz):
		fila.insert(0,' ') # Inserta en las filas de la Matriz tres columnas adicionales, en la segunda irá (en la fila que corresponda) la "H" como indicador
		fila.insert(0,' ') # de la palabra horizontal
		fila.insert(0,' ') 
	ancho_matriz = len(matriz[0])
	matriz.insert(0,[])	# Inserto dos filas en la Matriz, en la primera irán los indicadores de las palabras verticales y la segunda será un separador
	matriz.insert(0,[])
	for j in range(ancho_matriz):
		matriz[0].append(' ') 
		matriz[1].append(' ')
	contador_palabras_verticales = 0
	for vertical in verticales:
		contador_palabras_verticales += 1
		columna_de_cruce = informacion_de_verticales[vertical][0] + 3
		matriz[0][columna_de_cruce] = str(contador_palabras_verticales)
	matriz[fila_de_horizontal+2][1] = 'H'
	return matriz

def imprimir_definiciones(diccionario,horizontal,verticales):
	''' Recibe un Diccionario de palabras, una palabra horizontal y una lista de palabras verticales
		Imprime por pantalla las definiciones de cada palabra, indicando a qué palabra corresponde cada definición
	'''
	print(' DEFINICIONES')
	print()
	print(' H - {}'.format(diccionario[horizontal]))
	numerador = 0
	for vertical in verticales:
		numerador += 1
		print(' {} - {}'.format(numerador,diccionario[vertical]))


def incluir_solucion():
	''' Devuelve True si el usuario del programa elige ver las soluciones del crucigrama, False en caso contrario'''
	parser = argparse.ArgumentParser(description='Generador de crucigramas')
	parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solución')
	args = parser.parse_args()
	imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s
	return imprimir_solucion


