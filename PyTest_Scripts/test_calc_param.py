import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_addition(a,b,expected):
    assert a+b==expected


@pytest.mark.parametrize("x, y, result", [
    (10, 2, 5),
    (9, 3, 3),
    (12, 4, 3),
])
def test_division(x, y, result):
    assert x / y == result


# @pytest.mark.parametrize("a, b, expected", [
#     (5, 5, 11),  # wrong on purpose
# ])
# def test_failing_example(a, b, expected):
#     assert a + b == expected
