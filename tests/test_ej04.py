import pytest
from src.ej04_def2 import grados_celsius

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (105, 40.56),
        (100, 37.78),
        (32, 0.0)
    ]
)
def test_grados_celsius(input_x, expected):
    assert grados_celsius(input_x) == expected