def burro(image): #c
    iter = [] #c

    image.append(-1) #c

    for i in range(len(image)): #n
        iter_int = [image[-1]] + image[:-1] #n**2
        iter.append(iter_int) #n
        image = iter_int #n

    answer = [] #c

    iter.sort() #n**2 * logn
    for inter_int in iter: #n
        answer.append(inter_int[-1]) #n


    return answer #c
#Luego la complejidad de burro() es n**2 * logn, con n la longitud de la lista image

def rle(b, dim = None): # c
    n = len(b) # c
    res = [] # c
    i = 0 # c
    if (dim != None): # c
        res.append(str(dim) + ".") # c
    while (i < n-1): # n
        res.append(str(b[i])+",") # n
        count = 1 # n
        while(i < n-1 and b[i] == b[i + 1]): # Es dependiente de i luego continua siendo n
            count = count + 1 #n
            i = i + 1 #n
        res.append(str(count)+",") #n
        i = i +1 # n

    return "".join(res)[:-1] # c
#luego la complejidad de rle es n, con n la longitud de la lista b
def inverseRle(string): # c
    res = [] # c
    lista = string.split(",") # c
    n = len(lista) #c
    i = 0 # c
    while(i < n -1): #n
        res = res + [lista[i]]*int(lista[i+1]) #n
        i = i + 2 #n
    
    return res #n
#Luego la complejidad de inverseRle es n, con n la longitud de la string descomprimida

def antiBurro(B): #c
    
    #Indexar los caracteres de la ultima fila fin
    fin = [(B[i], i) for i in range(len(B))] # n
    #print("fin es ", fin)

    #Obtener la primera columna inicio
    inicio = sorted(fin) # nlogn
    #print("inicio es ", inicio)

    #Generar la lista ciclo que representa el circulo de iteracion
    ciclo = [] #c

    #Agregar -1 a ciclo sin index
    ciclo.append(inicio[0][0]) #c
    #print("ciclo es ", ciclo)

    #Definir -1 como el caracter actual
    actual = inicio[0] #c
    #print("actual es ", actual)

    while(len(ciclo) < len(B)): #n

        #Encontrar el index de actual en fin
        indexActualFin = actual[1]#n

        #Encontrar el caracter anterior 
        anterior = inicio[indexActualFin] #n
        #print("anterior es ", anterior)

        #Agregar anterior a respuesta sin index
        ciclo.append(anterior[0]) #n
        #print("ciclo es ", ciclo)

        #definir anterior como actual
        actual = anterior #n
        #print("actual es ", actual)

    return ciclo[1:] #c
#Luego la complejidad de antiBurro es n, con n la longitud de B


def lossless(image): #c

    ans = [] #c
    for col in image: #n
        col = burro(col) #n*m**2 * logm
        col = rle(col) #n*m
        ans += [col] #n

    return str(ans) #c
#Luego la complejidad de lossless es n* m**2 * logm, con n el numero de filas y m el numero de columnas
def dicompress(image): #c

    ans = [] #c

    for col in image: #n
        col = inverseRle(col) #n*m
        col = antiBurro(col) #n*m
        ans.append(col)#n
  
    return ans #c
#Luego la complejidad de dicompress es n*m, con n el numero de filas y m el numero de columnas
