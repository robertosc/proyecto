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
		if df['data2'][i] not in lista_hablantes:
			lista_hablantes.append(df['data2'][i])
	return lista_hablantes

def dict_promedio_todos(df, lista_hablantes):

	estadisticas = {}

	for j in range(len(lista_hablantes)):
		lista_tiempos = []
		for k in range(len(df)):
			if df['data2'][k] == lista_hablantes[j]:
				tiempo_habla = abs(-df['data0'][k] + df['data1'][k])
				lista_tiempos.append(tiempo_habla)
		promedio(lista_tiempos, lista_hablantes, j, estadisticas)
	return estadisticas

def dict_total_todos(df, lista_hablantes):
	total = {}

	for j in range(len(lista_hablantes)):
		lista_tiempos = []
		for k in range(len(df)):
			if df['data2'][k] == lista_hablantes[j]:
				tiempo_habla = abs(-df['data0'][k] + df['data1'][k])
				lista_tiempos.append(tiempo_habla)
		tiempo_total(lista_tiempos, lista_hablantes, j, total) #Añade elementos a total
	return total

def genero(df, lista_hablantes, dict_tiempos):
	'''
	Genera una lista con los hablantes hombres y hablantes mujeres.
	'''
	hombres = []
	mujeres = []
	total = 0
    
	for i in range(len(lista_hablantes)):
		#total += dict_tiempos[lista_hablantes[i]]
		if lista_hablantes[i][len(lista_hablantes[i])-1] == "M" or lista_hablantes[i][len(lista_hablantes[i])-1] == "m":
			mujeres.append(dict_tiempos[lista_hablantes[i]])
		elif lista_hablantes[i][len(lista_hablantes[i])-1] == "H" or lista_hablantes[i][len(lista_hablantes[i])-1] == "h":
			hombres.append(dict_tiempos[lista_hablantes[i]])

	#print(hombres)
	
	suma_h = sum(hombres)
	suma_m = sum(mujeres)
	prom_hombres = (suma_h*100) / (suma_h+suma_m)
	prom_mujeres = (suma_m*100) / (suma_h+suma_m)
	#results = {"Hombres" : prom_hombres, "Mujeres" :  prom_mujeres}
	print(len(lista_hablantes), "Hombres " ,len(hombres),": ", prom_hombres, "Mujeres ", len(mujeres), ": ", prom_mujeres)

def multiples_archivos(argv):
	for i in range(1, len(sys.argv)):
		filename = sys.argv[i]
		df = pd.read_csv(filename, sep='\t', engine='python', header=None, prefix="data")
		lista_hablantes = hablantes(df)
		print("Archivo: ", sys.argv[i], "\n\nCantidad de hablantes: ", len(hablantes(df)),  "\n\nTiempo promedio de intervención:\n", dict_promedio_todos(df,lista_hablantes), "\n\nTiempo total del habla:\n", dict_total_todos(df, lista_hablantes),  "\n")
		print("\n","Hombres y mujeres:" , genero(df, lista_hablantes, dict_total_todos(df,lista_hablantes)), "\n\n")
		print("-"*50)
		print("\n\n\n")

def main(argv):
	multiples_archivos(argv)

main(sys.argv)
