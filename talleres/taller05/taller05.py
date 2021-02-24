#!/usr/bin/python
import random
from matplotlib import pyplot as pl
import time

def array_generator(leng):
    """List generator"""
    return list(range(leng,0,-1))



#def array_sum(array, sum = 0):
"""Add the elements in the list"""


def multiplication_tables(n):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            print (str(i) + " * " + str(j) + " = " + str(i*j))
        print ("--------------------")

def insertion_sort(lst):
    temp = 0; #c1
    for i in range(1,len(lst)): #T1(n) = c2n
        for j in range(i,0,-1): #T2(n) = c3n*n
            if(lst[j] < lst[j-1]): #c4n*n
                temp = lst[j] #c4n*n
                lst[j] = lst[j-1] #c4n*n
                lst[j-1] = temp #c4n*n
                j = j -1 #c4n*n
            else: #c5
                break #c5
# One gets O(n**2)

#def arrayMax(arr):
#    return arrayMax_aux(arr, 0, 0)

#def arrayMax_aux(arr, i, max):


#-----------------------------GroupSum----------------------------------#

#def groupSum_aux(list, start, target):

def groupSum(lst): 
    cont = 0 #c1
    for i in lst: #c2n
        cont = cont + i #c3n
    return cont #c4

# One gets O(n) 


#----------------------------Fibonacci---------------------------------#

#def fib_r(n):                             #Fibonacci recursivo


#------------------------------Graphycs--------------------------------#

def graph(function, n, name, color, X = [],Y = [],Z = []):
    #Enter the function to test in attribute "function"
    #Enter the number of iterations do you want to try in "n"
    #Enter the color of the plot like this red: 'r', blue: 'b'

    for i in range(n):
        X.append(i)
        t = time.time()
        Z.append(function(i))
        Y.append(time.time()-t)

    print(Z) #this print all i's fibonacci i a  list
    pl.xlabel("N'simo" +  name)
    pl.ylabel('Tiempo de ejecucion')
    pl.title(name)
    pl.plot(X,Y,color, label = name) # domain of x(n) vs time
    pl.legend()
    pl.savefig(name + ".png")  # produce a .png file
    pl.show()

tiempo = []
iteraciones = []
res = []

for i in range(0,30000000,1500000):
    array = array_generator(i)
    print(len(array))
    iteraciones.append(i)
    t = time.time()
    res.append(groupSum(array)) #function evaluated
    tiempo.append(time.time() - t)


pl.xlabel("n array")
pl.ylabel("Tiempo de ejecucion")
pl.title("groupSum")
pl.plot(iteraciones, tiempo, 'r', label = "")
pl.legend((''))
#pl.savefig("ArrayMax.png")
pl.show

# graph(groupSum, 20, "", 'b')
