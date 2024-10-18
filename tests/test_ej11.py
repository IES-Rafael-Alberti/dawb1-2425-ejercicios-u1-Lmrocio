import pytest
from src.ej11_def import suma_final

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (10, 45),
        (7, 21),
    ]
)
def test_grados_celsius(input_x, expected):
    assert suma_final(input_x) == expected