from collections import deque

def brokenKeyboard(text): # c1
    deq = deque() #c2
    section = "" #c3
    actionDic = {"start": deq.appendleft, "end": deq.append}#c4
    key = "start"#c5
    for letter in text:#n*c6
        if(letter == "["):#n*c7
            actionDic[key](section)#n*c8
            section = ""#n*c9
            key = "start"#n*c10
        elif(letter == "]"):#n*c11
            actionDic[key](section)#n*c12
            section = ""#n*c13
            key = "end"#n*c14
        else:#n*c15
            section = section + letter#n*c16
    actionDic[key](section)#c17
    for section in deq:#n*c18
        print(section,end = "")#n*c19

"""
We get for the worst case
T(n) = c1 + c2 + c3 + c4 + c5 + n*c6 + n*c7 + n*c8 + n*c9 + n*c10 + c 17 + n*c18  + n*c19

With n the length of the string text

Note that for the final part of the algorithm, where the sections are printed, 
we know that the number of sections is equal or smaller than the length of the string 

Then
T(n) = O(n)

"""

brokenKeyboard("Aku")
