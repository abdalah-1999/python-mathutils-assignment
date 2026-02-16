import math
import pytest
from math_utils import MathUtils

@pytest.fixture
def mu():
    return MathUtils

def test_add(mu):
    assert mu.add(2, 3) == 5
    assert mu.add(-1, 1) == 0

def test_subtract(mu):
    assert mu.subtract(10, 3) == 7
    assert mu.subtract(3, 10) == -7

def test_multiply(mu):
    assert mu.multiply(4, 5) == 20
    assert mu.multiply(-3, 2) == -6

def test_divide(mu):
    assert mu.divide(10, 2) == 5.0
    assert mu.divide(3, 2) == 1.5

def test_divide_by_zero(mu):
    assert mu.divide(10, 0) == -1.0
    assert mu.divide(0, 0) == -1.0

def test_divide_precision(mu):
    assert math.isclose(mu.divide(1, 3), 1/3, rel_tol=1e-12)
