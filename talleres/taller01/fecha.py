class Fecha():
    
    def __init__(self,dia, mes, anyo):
        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo
      
    def dia(self):
        return self.__dia
      
    def mes(self):
        return self.__mes
          
    def anyo(self):
        return self.__anyo
          
    def comparar(self, otra):
        self_num = self.__str__().split("/")
        otra_num = otra.__str__().split("/")
        self_num.reverse()
        otra_num.reverse()
        self_num = int("".join(self_num))
        otra_num = int("".join(otra_num))
        
        if(self_num > otra_num):
            return 1
        elif(self_num < otra_num):
            return -1
        else:
            return 0
          
    def __str__(self): 
        self_dia_str = str(self.__dia) if self.__dia >= 10 else "0" + str(self.__dia)
        self_mes_str = str(self.__mes) if self.__mes >= 10 else "0" + str(self.__mes)
        self_anyo_str = str(self.__anyo)
        
        return self_dia_str + "/" + self_mes_str + "/" + self_anyo_str
