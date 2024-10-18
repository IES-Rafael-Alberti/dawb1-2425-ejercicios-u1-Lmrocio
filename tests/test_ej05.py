import pytest
from src.ej05_def2 import calcula_precio

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (100, -1, (1.21, 121)),
        (100, 15, (1.15, 115)),
    ]
)
def test_grados_celsius(input_x, input_y, expected):
    assert calcula_precio(input_x, input_y) == expected