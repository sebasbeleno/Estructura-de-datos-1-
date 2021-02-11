def hanoi(topN, a = "Tower1", b = "Tower2", c = "Tower3"):
    if(topN == 1):
        print("Disco " + str(topN) + " de " + a + " a " + b)
        return
    hanoi(topN-1, a, c, b)
    print("Disco " + str(topN) + " de " + a + " a " + b)
    hanoi(topN-1, c,b , a)
hanoi(4, "1", "3", "2")
"""def subset(s, base = ""):
  
def permutations(base, stri):"""
