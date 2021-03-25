from collections import deque


def polaca(entrada):
      entrada = entrada.split()
      pila = deque()
      operadores = "+*/-"      
      for i in range(0, len(entrada)):
          if entrada[i] in operadores:
             elDeArriba = pila.pop()
             elPenultimo = pila.pop()
             operador = entrada[i]
             if operador == '+':
                 pila.append(elPenultimo + elDeArriba)
             elif operador == '-':
                 pila.append(elPenultimo - elDeArriba)
             elif operador == '*':
                 pila.append(elPenultimo * elDeArriba)
             else: 
                 pila.append(elPenultimo / elDeArriba)
          else:
            pila.append(int(entrada[i]))
      return pila.pop()

#-------------------------------------------------------------------------

#Turns a list into a deque and returns
def toDeque(lista): 
    d = deque()
    for obj in lista:
        d.append(obj)
    return d
#Return a list with every solicitud paired with the corresponding fridges 
def asignarSolicitudes(neveras,solicitudes):
    result = [] #list to return
    neverasPerSolicitud = [] #fridges given to each store
    count = 0
    while(solicitudes):
        sol = solicitudes.popleft() #first in first out
        while(count < sol[1] and neveras):
            if(neveras):
                neverasPerSolicitud.append(neveras.pop()) #first in last out
                count = count + 1
            else:
                break;
        result = result +  [(sol[0], neverasPerSolicitud)]
        neverasPerSolicitud = []
        count = 0
    return result
        
        
almacen = [(1,"haceb"), (2,"lg"), (3,"ibm"), (4,"haceb"), 
(5,"lg"), (6,"ibm"),(7,"haceb"), (8,"lg"), (9,"ibm"),(8,"lg"), 
(9,"ibm")] #9 ibm was the last element added (stack)

solicitudes = [("eafit", 10), ("la14", 2), ("olimpica", 4), 
("éxito", 1)] #exito was the first element added (queue)

solicitudes.reverse() #Since is queue we need to change the order for the toDeque method (queue)

almacen = toDeque(almacen)
solicitudes = toDeque(solicitudes)

result = asignarSolicitudes(almacen, solicitudes)
print("")
for sol in result:
    print(sol)


    