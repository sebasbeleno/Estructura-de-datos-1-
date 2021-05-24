def burro(image):
    iter = []

    image.append(-1)

    for i in range(len(image)):
        iter_int = [image[-1]] + image[:-1]
        iter.append(iter_int)
        image = iter_int 

    answer = []

    iter.sort()
    for inter_int in iter:
        answer.append(inter_int[-1])


    return answer

def rle(b, dim = None):
    n = len(b)
    res = []
    i = 0
    if (dim != None):
        res.append(str(dim) + ".")
    while (i < n-1):
        res.append(str(b[i])+",")
        count = 1
        while(i < n-1 and b[i] == b[i + 1]):
            count = count + 1 
            i = i + 1
        res.append(str(count)+",")
        i = i +1

    return "".join(res)[:-1]

def inverseRle(string): 
    res = []
    lista = string.split(",")
    n = len(lista)
    i = 0
    while(i < n -1):
        res = res + [lista[i]]*int(lista[i+1])
        i = i + 2
    
    return res

def antiBurro(B):
    
    #Indexar los caracteres de la ultima fila fin
    fin = [(B[i], i) for i in range(len(B))]
    #print("fin es ", fin)

    #Obtener la primera columna inicio
    inicio = sorted(fin)
    #print("inicio es ", inicio)

    #Generar la lista ciclo que representa el circulo de iteracion
    ciclo = []

    #Agregar -1 a ciclo sin index
    ciclo.append(inicio[0][0])
    #print("ciclo es ", ciclo)

    #Definir -1 como el caracter actual
    actual = inicio[0]
    #print("actual es ", actual)

    while(len(ciclo) < len(B)):

        #Encontrar el index de actual en fin
        indexActualFin = actual[1]

        #Encontrar el caracter anterior 
        anterior = inicio[indexActualFin]
        #print("anterior es ", anterior)

        #Agregar anterior a respuesta sin index
        ciclo.append(anterior[0])
        #print("ciclo es ", ciclo)

        #definir anterior como actual
        actual = anterior
        #print("actual es ", actual)

    return ciclo[1:]

def antiBurro(B):
    
    #Indexar los caracteres de la ultima fila fin
    fin = [(B[i], i) for i in range(len(B))]
    #print("fin es ", fin)

    #Obtener la primera columna inicio
    inicio = sorted(fin)
    #print("inicio es ", inicio)

    #Generar la lista ciclo que representa el circulo de iteracion
    ciclo = []

    #Agregar -1 a ciclo sin index
    ciclo.append(inicio[0][0])
    #print("ciclo es ", ciclo)

    #Definir -1 como el caracter actual
    actual = inicio[0]
    #print("actual es ", actual)

    while(len(ciclo) < len(B)):

        #Encontrar el index de actual en fin
        indexActualFin = actual[1]

        #Encontrar el caracter anterior 
        anterior = inicio[indexActualFin]
        #print("anterior es ", anterior)

        #Agregar anterior a respuesta sin index
        ciclo.append(anterior[0])
        #print("ciclo es ", ciclo)

        #definir anterior como actual
        actual = anterior
        #print("actual es ", actual)

    return ciclo[1:]

def lossless(image):

    ans = []
    for col in image:
        col = burro(col)
        col = rle(col)
        ans += [col]

    return str(ans) 

def dicompress(image):

    ans = []

    for col in image:
        col = inverseRle(col)
        col = antiBurro(col)
        ans.append(col)
    
    return ans