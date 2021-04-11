# Punto 1
print('Punto 1:')
class HashTable():
    
    def __init__(self):
        self.tabla = []
        for i in range(10):
            self.tabla.append([])

    # Noob exampleHash_function
    def funcionHash(self, k):
        totalSum = 0
        for i in range(len(k)):
            totalSum = (ord(k[i])*(32**(len(k)-i-1))) + totalSum
        return totalSum%len(self.tabla)

    def get(self, k):
        aux = self.tabla[self.funcionHash(k)]
        for t in aux:
            if t[0] == k:
                return t[1]
        return None

    def put(self, k, v):       
        self.tabla[self.funcionHash(k)].append((k, v))

exampleHash = HashTable()
exampleHash.put('Aku', 666)
exampleHash.put('samurai', 777)
print(exampleHash.get('Aku'))
print(exampleHash.get('samurai'))
print(exampleHash.get('magicSword'))
print(exampleHash.tabla)

# Punto 2
print('Punto 2:')
empresas = {'Google': 'Estados Unidos',
            'La Locura': 'Colombia',
            'Nokia': 'Finlandia',
            'Sony': 'Japon'}

for k, v in empresas.items():
    print(k, v) # Tuple

# Punto 3
print('Punto 3:')
print(empresas.get('Google'))
print(empresas.get('Motorola'))

# Punto 4
print('Punto 4:')
paises = empresas.values()
print('India' in paises)
print('Estados Unidos' in paises)