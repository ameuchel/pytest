import pytest

@pytest.mark.parametrize("a, b, b",
                        [(10, 20, 200),
                         (20, 40, 200)
                         ]
                         )
def test_method(a, b, c):
    assert a*b == c