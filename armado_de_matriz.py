''' En este Módulo:
. Se dimensiona la Matriz
. Se cruzan las palabras dentro de la Matriz y se terminan de definir sus posiciones
. Finalmente, se rellena la Matriz de acuerdo a los datos obtenidos en los otros métodos
'''
from generacion_de_crucigramas import agregar_indicadores


def dimensionar_matriz(horizontal,verticales):
	''' Recibe una palabra horizontal y una lista de palabras verticales
		Devuelve una Matriz con suficientes filas y columnas para contener a las palabras recibidas (se asegura de que entren en cualquier caso)
	'''
	numero_de_filas = 0
	for palabra in verticales:
		if len(palabra) * 2 > numero_de_filas:
			numero_de_filas = len(palabra) * 2
	numero_de_columnas = len(horizontal)
	matriz = []
	for i in range(numero_de_filas):
		nueva_fila = []
		for j in range(numero_de_columnas):
			nueva_fila.append(' ')
		matriz.append(nueva_fila)
	return matriz

def cruzar_palabras(horizontal,fila_de_horizontal,verticales,informacion_de_verticales):
	''' Recibe una palabra horizontal, la posición de su fila en una Matriz, una lista de palabras verticales y un diccionario con información sobre las mismas
		Devuelve el mismo Diccionario que ingresó, pero agregándole más información sobre la ubicación de las palabras verticales en una Matriz
	'''
	for vertical in verticales:
		columna_de_cruce = informacion_de_verticales[vertical]
		fila_de_cruce = vertical.index(horizontal[columna_de_cruce])
		fila_inicial = fila_de_horizontal - fila_de_cruce 				# fila donde empezará a rellenarse la matriz para la palabra en vertical
		fila_final = fila_de_horizontal + ( len(vertical) - fila_de_cruce) 
		total_filas = fila_final - fila_inicial 						# cantidad de filas que ocupará la palabra
		informacion_de_verticales[vertical] = [columna_de_cruce,fila_inicial,total_filas]


def rellenar_matriz(diccionario,horizontal,verticales,informacion_de_verticales):
	''' Recibe una palabra horizontal, la posición de su fila en una Matriz, una lista de palabras verticales y un diccionario con información sobre las mismas
		Devuelve una Matriz a partir de la cual se puede generar un crucigrama
	'''
	matriz = dimensionar_matriz(horizontal,verticales)
	fila_de_horizontal = len(matriz) // 2 + len(matriz) % 2			# determina la fila de la Matriz en la que irá ubicada la palabra horizontal
	cruzar_palabras(horizontal,fila_de_horizontal,verticales,informacion_de_verticales)
	ancho_matriz = len(matriz[0])		
	for i in range(ancho_matriz):
		matriz[fila_de_horizontal][i] = horizontal[i]				# agrega las letras de la palabra horizontal a su correspondiente espacio en la Matriz
	for vertical in verticales:
		columna_de_cruce = informacion_de_verticales[vertical][0]	
		fila_inicial = informacion_de_verticales[vertical][1]
		total_filas = informacion_de_verticales[vertical][2]
		for i in range(total_filas):
			matriz[fila_inicial+i][columna_de_cruce] = vertical[i] # agrega las letras de las palabras verticales a su correspondiente espacio en la Matriz
	matriz,fila_de_horizontal = eliminar_filas_innecesarias(matriz,fila_de_horizontal)
	agregar_indicadores(matriz,horizontal,fila_de_horizontal,verticales,informacion_de_verticales)
	return matriz

def eliminar_filas_innecesarias(matriz,fila_de_horizontal):
	''' Recibe una matriz y la posición de la palabra horizontal en esa Matriz
		Devuelve una nueva matriz, sin filas innecesarias (es decir, sin ninguna letra) y la nueva posición de la palabra horizontal.
	'''
	fila_palabra_horizontal = matriz[fila_de_horizontal]    # Toma la Fila de la Palabra Horizontal de la Matriz original para compararla luego
	nueva_matriz = []
	for i,fila in enumerate(matriz):		
		for posicion in fila:
			if posicion != ' ':								# Pasa a la Nueva Matriz cualquier fila con por lo menos una letra
				nueva_matriz.append(fila)
				break
	fila_de_horizontal = len(nueva_matriz) // 2 + len(nueva_matriz) % 2
	for i,fila in enumerate(nueva_matriz):
		if fila == fila_palabra_horizontal:                  # Si la fila es igual a la de la Horizontal original, entonces es la nueva Fila De Horizontal
			fila_de_horizontal = i
	return nueva_matriz,fila_de_horizontal