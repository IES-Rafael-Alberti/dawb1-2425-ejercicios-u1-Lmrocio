import pytest
from src.prueba1 import comparacion_num

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (0, 0, 0),
        (2, 1, 2),
        (1, 2, 2)
    ]
)

def test_suma_params(input_x, input_y, expected):
    assert comparacion_num(input_x, input_y) == expected