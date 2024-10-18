import pytest
from src.ej02_def import salario

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (2, 3, 6),
        (2, 1, 2),
        (2, 2, 4)
    ]
)
def test_salario(input_x, input_y, expected):
    assert salario(input_x, input_y) == expected