def gcd_euclid(b, a):
    if(b > a):
        if (b%a == 0):
            return a
        else:
            return gcd_euclid(b, b%a)
    else:
        if (a%b == 0):
            return b
        else:
            return gcd_euclid(a, a%b)


print(gcd_euclid(60, 48))