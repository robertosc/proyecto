import pandas as pd
import sys

def tiempo_total(lista_tiempos, lista_hablantes, index, dict_total):
	'''
	Calcula el tiempo total que habla cada persona del programa
	'''
	total = 0
	for i in range(len(lista_tiempos)):
		total+=lista_tiempos[i]
	dict_total[lista_hablantes[index]] = total

def promedio(lista_tiempos, lista_hablantes, index ,dict_estadisticas):
	'''
	Calcula el promedio que tardan las intervenciones de cada persona
	'''
	total = 0
	for i in range(len(lista_tiempos)):
		total+=lista_tiempos[i]
	promedio = total/len(lista_tiempos)
	dict_estadisticas[lista_hablantes[index]] = promedio

def hablantes(df):
	'''
	Genera con todos los hablantes del programa
	'''
	lista_hablantes = []
	for i in range(len(df)):
		if df['Speaker'][i] not in lista_hablantes:
			lista_hablantes.append(df['Speaker'][i])
	return lista_hablantes

def dict_promedio_todos(df, lista_hablantes):

	estadisticas = {}

	for j in range(len(lista_hablantes)):
		lista_tiempos = []
		for k in range(len(df)):
			if df['Speaker'][k] == lista_hablantes[j]:
				tiempo_habla = -df['Start'][k] + df['End'][k]
				lista_tiempos.append(tiempo_habla)
		promedio(lista_tiempos, lista_hablantes, j, estadisticas)
	return estadisticas

def dict_total_todos(df, lista_hablantes):
	total = {}

	for j in range(len(lista_hablantes)):
		lista_tiempos = []
		for k in range(len(df)):
			if df['Speaker'][k] == lista_hablantes[j]:
				tiempo_habla = -df['Start'][k] + df['End'][k]
				lista_tiempos.append(tiempo_habla)
		tiempo_total(lista_tiempos, lista_hablantes, j, total)
	return total

def genero(df, lista_hablantes):
	'''
	Genera una lista con los hablantes hombres y hablantes mujeres.
	'''
	hombres = []
	mujeres = []
	for i in range(len(lista_hablantes)-1):
		if lista_hablantes[i][len(lista_hablantes[i])-1] == "M" or lista_hablantes[i][len(lista_hablantes[i])-1] == "m":
			mujeres.append(lista_hablantes[i])
		elif lista_hablantes[i][len(lista_hablantes[i])-1] == "H" or lista_hablantes[i][len(lista_hablantes[i])-1] == "h":
			hombres.append(lista_hablantes[i])
	
	print(hombres, mujeres)

def multiples_archivos(argv):
	for i in range(1, len(sys.argv)):
		filename = sys.argv[i]
		df = pd.read_csv(filename, sep='\t', engine='python')
		lista_hablantes = hablantes(df)
		print("Archivo: ", sys.argv[i], "\n\nTiempo promedio de habla:\n", dict_promedio_todos(df,lista_hablantes), "\n\nTiempo total del habla:\n", dict_total_todos(df, lista_hablantes),  "\n\n")




def main(argv):
	multiples_archivos(argv)


#filename = "/mnt/c/Users/rober/OneDrive/Documentos/20200312_desayunos_parte2_estadistica.segments"
#df = pd.read_csv(filename, sep='\t', engine='python')

main(sys.argv)
#genero(df, hablantes(df))
