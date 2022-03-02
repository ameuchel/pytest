import pytest

@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 30
    return [a, b, c]

def test_method1(numbers):
    x = 15
    assert numbers[0] == x

# @pytest.mark.skip would skip the test
def test_method2(numbers):
    y = 20
    assert numbers[1] == y

# @pytest.mark.skip would skip the test
def test_method3(numbers):
    z = 30
    assert numbers[2] == z