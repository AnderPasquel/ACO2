import sys
import random
from math import *

def probabilidadAristas(distancia, feromona, aristas_visitadas):
	apt = 0
	#print("Sumatoria: ")
	for x in range(len(distancia)):
		if(aristas_visitadas[x] == 1):
			apt += 0
			#print(apt)
		else:
			apt += (1/distancia[x]*feromona[x])
			#print(apt)

	aristas = []
	for i in range(len(distancia)):
		if(aristas_visitadas[i] == 1):
			aristas.append(0)
		else:
			aristas.append(round(((1/distancia[i]*feromona[i])/apt)*100, 0))

	return aristas

def ruletaSeleccion(probabilidad, aristas_visitadas, recorrido, distancia, ubicacion, feromona, recorrido_hormigas):
	rangos = []
	rangos.append(probabilidad[0])
	for i in range (len(probabilidad)-1):
		rangos.append(rangos[i]+probabilidad[i+1])

	#print("Rangos asignados: ", rangos)

	y = random.randint(1, 100)
	#print("Número ganador: ", y)

	if(y >= 1 and y <= rangos[0]):
		recorrido.append(rangos.index(rangos[0]))
		recorrido_hormigas[ubicacion][0] += 1
		for a in range(len(aristas_visitadas)):
			aristas_visitadas[a][0] = 1
		return rangos.index(rangos[0]), distancia[ubicacion][0]
		'''--------------------------'''
	elif(y > rangos[0] and y <= rangos[1]):
		recorrido.append(rangos.index(rangos[1]))
		recorrido_hormigas[ubicacion][1] += 1
		for a in range(len(aristas_visitadas)):
			aristas_visitadas[a][1] = 1
		return rangos.index(rangos[1]), distancia[ubicacion][1]
		'''--------------------------'''
	elif(y > rangos[1] and y <= rangos[2]):
		recorrido.append(rangos.index(rangos[2]))
		recorrido_hormigas[ubicacion][2] += 1
		for a in range(len(aristas_visitadas)):
			aristas_visitadas[a][2] = 1
		return rangos.index(rangos[2]), distancia[ubicacion][2]
		'''--------------------------'''
	elif(y > rangos[2] and y <= rangos[3]):
		recorrido.append(rangos.index(rangos[3]))
		recorrido_hormigas[ubicacion][3] += 1
		for a in range(len(aristas_visitadas)):
			aristas_visitadas[a][3] = 1
		return rangos.index(rangos[3]), distancia[ubicacion][3]
		'''--------------------------'''
	elif(y > rangos[3] and y <= rangos[4]):
		recorrido.append(rangos.index(rangos[4]))
		recorrido_hormigas[ubicacion][4] += 1
		for a in range(len(aristas_visitadas)):
			aristas_visitadas[a][4] = 1
		return rangos.index(rangos[4]), distancia[ubicacion][4]
		'''--------------------------'''
	elif(y > rangos[4] and y <= rangos[5]):
		recorrido.append(rangos.index(rangos[5]))
		recorrido_hormigas[ubicacion][5] += 1
		for a in range(len(aristas_visitadas)):
			aristas_visitadas[a][5] = 1
		return rangos.index(rangos[5]), distancia[ubicacion][5]

def actualizarFeromona(feromona, tasa_evaporacion, constante_deposito, longitud_recorrido, recorrido_hormigas):
	for f in range(len(feromona)):
		for m in range(len(feromona[f])):
			suma = 0
			if(recorrido_hormigas[f][m] == 0):
				suma = 0
			elif(recorrido_hormigas[f][m] != 0):
				for v in range(recorrido_hormigas[f][m]):
					suma += constante_deposito/longitud_recorrido
			
			feromona[f][m] = round((1 - tasa_evaporacion)*feromona[f][m]+suma, 3)

d = [[0, 8, 2, 33, 10, 20], [8, 0, 22, 17, 23, 5], [2, 22, 0, 17, 13, 3], [33, 17, 7, 0, 24, 15], [10, 23, 13, 24, 0, 6], [20, 5, 3, 15, 6, 0]]
t = [[0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0]]
visitadas = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
p_hormigas = [[2, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 2]]
hormigas = 2
Lk = 6
p = 0.3
Q = 1
max_iter = 1
camino = []

d = list(d)
t = list(t)
p_hormigas = list(p_hormigas)
iter = 1
while(iter <= max_iter):
	print("-----------------------------------------------------------------------")
	print("ITERACION NO. ", iter)
	print("-----------------------------------------------------------------------")
	h = 1
	comp = []
	while(h <= hormigas):
		print("HORMIGA NO. ", h)
		print("-----------------------------------------------------------------------")
		route = []
		camino = []
		ubc = 0
		tot = 0
		route = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
		ubc = random.randint(0, 5)
		camino.append(ubc)
		for r in range(len(route)):
			route[r][ubc] = 1
		n = 1
		while(n < Lk):
			print("Ubicación actual: ", ubc)
			ubc, std = ruletaSeleccion(probabilidadAristas(d[ubc], t[ubc], route[ubc]), route, camino, d, ubc, t, p_hormigas)
			print("Arista seleccionada: ", ubc)
			#print("Distancia de la arista seleccionada: ", std)
			#print("Aristas visitadas: ", route)
			print("Recorrido hasta ahora: ", camino)
			#print("Aristas y su cantidad de hormigas que pasaron por ella: ", p_hormigas)
			n=n+1
			tot += std
			print("")
			#print("Iteraciones: ", n)

		print("Longitud del recorrido del la hormiga no. ", h, ": ", tot)
		print("-----------------------------------------------------------------------")
		comp.append(tot)
		h=h+1
	print("Hormiga con el recorrido mas eficiente: ", comp.index(min(comp))+1)
	print("")
	actualizarFeromona(t, p, Q, Lk, p_hormigas)
	print("Feromonas actualizadas: ", t)
	iter=iter+1