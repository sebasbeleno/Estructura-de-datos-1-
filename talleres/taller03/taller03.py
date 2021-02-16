def hanoi(topN, a = "Tower1", b = "Tower2", c = "Tower3"):
    if(topN == 1):
        print("Disco " + str(topN) + " de " + a + " a " + b)
        return
    hanoi(topN-1, a, c, b)
    print("Disco " + str(topN) + " de " + a + " a " + b)
    hanoi(topN-1, c,b , a)

def subset(s, base = ""):
    if len(s) == 0:
        print(base)
    else:
        subset(s[1:], base + s[0])
        subset(s[1:], base)

def permutations(s, base = ""):
    if len(s) == 0:
        print (base)
    else:
        i = 0
        while i < len(s):
            permutations(s[0:i] + s[i+1:], base + s[i], )
            i = i + 1
