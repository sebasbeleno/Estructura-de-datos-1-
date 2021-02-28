def rectangles(n):
    if(n <= 1): 
        return 1
    return rectangles(n-1) + rectangles(n-2) 
