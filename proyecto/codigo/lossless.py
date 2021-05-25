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
    while (i < n):
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
        res = res + [int(float(lista[i]))]*int(lista[i+1])
        i = i + 2
    return res



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

    return ans

def dicompress(image):

    ans = []

    for col in image:
        col = inverseRle(col)
        col = antiBurro(col)
        ans.append(col)
    
    return ans

    
    
"""
    __
___( o)>
\ <_. )
 `---'   hey o/. Im just another dock. Take a breath, my brave ingenier 

"""
