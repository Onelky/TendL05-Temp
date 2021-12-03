from app import Temperature
from temp_scale import TemperatureScale

def test_temptoF_0C_should_return_32F():
    celcius_temp = Temperature(0, TemperatureScale.C)
    assert celcius_temp.to_f() == 32
    

     
