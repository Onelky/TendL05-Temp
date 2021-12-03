from app import Temperature
from temp_scale import TemperatureScale


def test_to_f_0C_should_return_32F():
    celcius_temp = Temperature(0, TemperatureScale.C)
    assert celcius_temp.to_f() == 32


def test_to_k_0C_should_return_273K():
    celcius_temp = Temperature(0, TemperatureScale.C)
    assert celcius_temp.to_k() == 273.15


def test_to_c_32F_should_return_0C():
    fahrenheit_temp = Temperature(32, TemperatureScale.F)
    assert fahrenheit_temp.to_c() == 0


def test_to_k_32F_should_return_273_15K():
    fahrenheit_temp = Temperature(32, TemperatureScale.F)
    assert fahrenheit_temp.to_k() == 273.15


def test_to_c_300K_should_return_26_85C():
    kelvin_temp = Temperature(300, TemperatureScale.K)
    assert kelvin_temp.to_c() == 26.85


def test_to_f_300K_should_return_80_33F():
    kelvin_temp = Temperature(300, TemperatureScale.K)
    assert kelvin_temp.to_f() == 80.33
