import pytest
from src.ej01 import saludo

def test_saludo():
    assert saludo('Alejandro') == "Hola, Alejandro." 