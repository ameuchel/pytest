import pytest

@pytest.mark.one
def func(x):
    def test_func():
        assert func(3) == 8