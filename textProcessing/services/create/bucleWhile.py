def crearBucleWhile(instruccion):

	identificadores = ["mientras","cuando","condicion","variable","variables"]
	condicion = []
	for i in range(len(instruccion)):
		if instruccion[i] in identificadores:
			indice = i+1
			break
		indice = None

	if indice == None:
		return "Error no se encontro indice"
	else:
		for i in range (indice, len(instruccion)):
			condicion.append(instruccion[i])


	palabrasSobrantes = ["sean","sea","que","y","variable","variables","la","las",""]
	for i in reversed(range(len(condicion))):
		if condicion[i] in palabrasSobrantes:
				condicion.remove(condicion[i])
		if condicion[i] == "mayor":
				condicion[i] = ">"
		if condicion[i] == "menor":
				condicion[i] = "<"
		if condicion[i] == "igual" or condicion[i] == "iguales" or condicion[i] == "equivalente":
				condicion[i] = "=="
        
	sentenciaFinal = "while "
	for i in range(len(condicion)):
		if condicion[i] == "<" or condicion[i] == ">" or condicion[i] == "==":
			condicion[i], condicion[1] = condicion[1], condicion[i]

	for i in range(len(condicion)):
		sentenciaFinal = f"{sentenciaFinal} {condicion[i]}"

	sentenciaFinal = f"{sentenciaFinal}:"
	print(sentenciaFinal)