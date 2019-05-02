''' En este Módulo:
. Se genera el Diccionario desde el archivo
. Se elige la palabra horizontal
. Se eligen las palabras verticales de acuerdo a la horizontal
'''

from random import randint

def generar_diccionario(archivo):
	''' Recibe una ruta
		Devuelve un Diccionario generado a partir del contenido del archivo en esa ruta
	'''
	diccionario = {}
	with open(archivo, encoding="utf8") as archivo:
		for linea in archivo:
			palabra, significado = linea.split('|')
			diccionario[palabra] = significado
	return diccionario

def palabra_horizontal(diccionario):
	''' Recibe un Diccionario de palabras
		Devuelve al azar una palabra de 8 letras o más
	'''
	claves = diccionario.keys()
	posibles_horizontales = []
	for clave in claves:
		if len(clave) >= 8:
			posibles_horizontales.append(clave)
	numero_al_azar = randint(0,len(posibles_horizontales))
	palabra_horizontal = posibles_horizontales[numero_al_azar]
	return palabra_horizontal

def palabras_verticales(diccionario,horizontal):
	claves = diccionario.keys()
	posibles_verticales = []
	for letra in horizontal:
		verticales_por_letra = []						  # Por cada letra elegida de la palabra horizontal, arma una lista que contendrá palabras verticales...						
		for vertical in claves:							  # ... que pueden ser consideradas para esa letra	
			if letra in vertical:
				verticales_por_letra.append(vertical)     # Agrega palabras del diccionario que contengan a la letra de turno
		posibles_verticales.append(verticales_por_letra)
	verticales_elegidas = []							  # Arma una nueva lista, que esta vez contendrá las palabras verticales definitivas
	for verticales_por_letra in posibles_verticales:
		while True:
			numero_al_azar = randint(0,len(verticales_por_letra)-1)
			vertical_elegida = verticales_por_letra[numero_al_azar]
			if not (vertical_elegida in verticales_elegidas) and (vertical_elegida != horizontal):     # Verifica que no se repita ninguna palabra
				verticales_elegidas.append(vertical_elegida)
				break
	lista_de_posiciones = definir_posiciones(horizontal)
	verticales_definitivas = []
	for posicion in lista_de_posiciones:
		vertical_definitiva = verticales_elegidas[posicion]
		verticales_definitivas.append(vertical_definitiva)
	informacion_de_verticales = {}						  # Crea un diccionario cuyas claves son las palabras verticales y sus valores son su posición...
	for i in range(len(verticales_definitivas)):		  # ... respecto a la palabra horizontal (más adelante se agregará más información)
		informacion_de_verticales[verticales_definitivas[i]] = lista_de_posiciones[i]
	return verticales_definitivas,informacion_de_verticales

def definir_posiciones(horizontal):
	''' Recibe una palabra (denominada horizontal por su utilización en un futuro crucigrama)
		Devuelve: - una lista de posiciones en las que las palabras verticales se cruzarán con la horizontal
	'''
	lista_posiciones = [randint(0,2)]
	while True:												# Recorre las letras de la palabra horizontal, pero salteando una o dos (al azar), y va agregando
		pos_al_azar = randint(2,3)							# las letras y las posiciones de esas letras en la palabra horizontal a dos listas diferentes
		nueva_posicion = lista_posiciones[-1] + pos_al_azar
		if nueva_posicion >= len(horizontal):
			return lista_posiciones
		lista_posiciones.append(nueva_posicion)