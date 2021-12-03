
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
            return (self.value * 9/5) + 32

        elif(self.type == TemperatureScale.K):
            return (self.value - 273.15) * 9/5 + 32

        return self.value
