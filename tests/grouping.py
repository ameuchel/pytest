# class doesn't have to be called TestClass
# funcs must start with 'test' to be tested

# can run with pytest grouping.py


class TestClass:
    def test_one(self):
        x = 'this'
        assert 's' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, "check")