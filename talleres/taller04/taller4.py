#!/usr/bin/python
import random
from matplotlib import pyplot as plt
from time import time
import sys 

sys.setrecursionlimit(10**6)

x = []
y = []

def array_generator(ln):
    return [i for i in range(ln)]
    
def array_sum(array, s = 0):
    """Add the elements in the list"""
    if (s == len(array)):
        return 0
    else:
        return array[s] + array_sum(array, s +1)

def multiplication_tables(n):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            print (str(i) + " * " + str(j) + " = " + str(i*j))
        print ("--------------------")
  
def arrayMax(arr):
    return arrayMax_aux(arr, len(arr) -1)

def arrayMax_aux(arr, i):
    maxi = arr[i]
    if (i != 0):
        temp = arrayMax_aux(arr, i-1)
        if (temp > maxi):
            maxi = temp
    return maxi

def groupSum_aux(lst, start, target):
    if (start >= len(lst)):
        return target == 0
    return groupSum_aux(lst, start +1, target - lst[start]) or groupSum_aux(lst, start +1, target)

def groupSum(lst, target):
    return groupSum_aux(lst, 0, target)

#Mi computador no soporta valores mas grandes a los usados
#Numeros demaciado pequeños para ver un patron con una muestra de 20
#Por tanto se toma una muestra mayor a la indicada
for i in range(1, 3001 +1, 1):
    lst = array_generator(i)
    print("array lenght:", len(lst))
    x = x + [len(lst)]
    inicio = time()
    print(arrayMax(lst))
    fin = time()
    total = fin-inicio
    y = y + [total]
    print("The run time of the program is", total)

plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('array lenght') 
# naming the y axis 
plt.ylabel('execution time') 
  
# giving a title to my graph 
plt.title('array lenght vs execution time') 
  
# function to show the plot 
plt.show()

x =[]
y = []

for i in range(10, 26):
    print("array lenght:", i)
    lst = sorted(array_generator(i)) #se organiza de menor a mayor para garantizar el peor caso
    x = x + [len(lst)]
    inicio = time()
    print(groupSum(lst, 15.5)) #siempre es falso para evaluar el peor caso
    fin = time()
    total = fin-inicio
    y = y + [total]
    print("The run time of the program is", total)

plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('array lenght') 
# naming the y axis 
plt.ylabel('execution time') 
  
# giving a title to my graph 
plt.title('array lenght vs execution time') 
  
# function to show the plot 
plt.show()

