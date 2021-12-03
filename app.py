
# I)Lib + Package
#     val t=new Temperature(5.25, TemperatureScale.Celcius); // 1. Constructor

#     t.ToF(); // 2
#     t.ToC(); // 3
#     t.ToK(); // 4

#     - --------------------------
#     II) ConsoleApp
#    	Instalar el paquete

from temp_scale import TemperatureScale


class Temperature:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_f(self):
        if(self.type == TemperatureScale.C):
            return round((self.value * 9/5) + 32, 2)

        elif(self.type == TemperatureScale.K):
            return round((self.value - 273.15) * 9/5 + 32, 2)

        return self.value
    
    def to_k(self):
        if(self.type == TemperatureScale.C):
            return round(self.value + 273.15)

        elif(self.type == TemperatureScale.F):
            return 273.5 + ((self.value - 32.0) * (5.0/9.0))

        return self.value
    
    def to_c(self):
        if(self.type == TemperatureScale.F):
            return round((self.value - 32) * 5/9, 2)

        elif(self.type == TemperatureScale.K):
            return round(self.value - 273.15, 2)

        return self.value
       
