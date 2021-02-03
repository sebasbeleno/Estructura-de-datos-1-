
def subconjuntos(s):
    return subconjuntosBase("", s)
def subconjuntosBase(base, t):
    if(t == ""):
        return base
    return subconjuntosBase(base + t[0], t[1:]) + " " + subconjuntosBase(base, t[1:])

print(subconjuntos("Santi"))