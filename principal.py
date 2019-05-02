
''' Para una mejor organización, se dividió el código en tres módulos, de acuerdo a cada fase del programa'''

from seleccion_de_palabras import generar_diccionario,palabra_horizontal,palabras_verticales

from armado_de_matriz import rellenar_matriz

from generacion_de_crucigramas import generar_crucigramas,imprimir_definiciones,incluir_solucion


def main():
	diccionario = generar_diccionario(r"palabras.csv")
	horizontal = palabra_horizontal(diccionario)
	verticales,informacion_de_verticales = palabras_verticales(diccionario,horizontal)
	matriz = rellenar_matriz(diccionario,horizontal,verticales,informacion_de_verticales)
	crucigrama_con_soluciones,crucigrama_codificado = generar_crucigramas(matriz)
	print()
	print()
	for fila in crucigrama_codificado:
		print(fila)
	print()
	print()
	imprimir_definiciones(diccionario,horizontal,verticales)
	print()
	if incluir_solucion():
		for fila in crucigrama_con_soluciones:
			print(fila)
	


main()