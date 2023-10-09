import pytest
from solution import Solution
from functions import Functions
from slow import expensive_call

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# gens, points
test_solution = [
    (0, 0, 1),
    (0, 1, 1),
    (0, 10, 1),
    (0, -1, 1),
    (1, 0, 1),
    (10, 0, 1),
    (-1, 0, 1),
    (1, 1, 2),
    (10, 10, 11)
]

test_values = [
    (0, 0, [[5, 5]]),
    (0, 1, [[5, 5]]),
    (0, 10, [[5, 5]]),
    (0, -1, [[5, 5]]),
    (1, 0, [[5, 5]]),
    (10, 0, [[5, 5]]),
    (-1, 0, [[5, 5]])  # ,
    # Z hlediska nahodnosti blind_search algoritmu neni mocne presne urcit dalsi hodnoty
    # (1, 1, [[5, 5], [-1.5876541268399844, 1.7575629285798469]]),
    # (10, 10, [[5, 5], [1.440804722626571, -0.9286211934904101], [-0.9738933739222153, 0.7197258675364342], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759], [-0.370753588240607, 0.1417488516179759]])
]

test_levy = [
    ([0, 0], 0.5000000000000001),
    ([0, 1], 0.5000000000000001),
    ([0, 2], 0.5000000000000001),
    ([0, 3], 0.5000000000000001),
    ([0, 4], 0.5000000000000001),
    ([1, 0], 1.4997597826618576e-32),
    ([1, 1], 1.4997597826618576e-32),
    ([1, 2], 1.4997597826618576e-32),
    ([1, 3], 1.4997597826618576e-32),
    ([1, 4], 1.4997597826618576e-32),
    ([2, 0], 0.4999999999999999),
    ([2, 1], 0.4999999999999999),
    ([2, 2], 0.4999999999999999),
    ([2, 3], 0.4999999999999999),
    ([2, 4], 0.4999999999999999),
    ([3, 0], 1.0),
    ([3, 1], 1.0),
    ([3, 2], 1.0),
    ([3, 3], 1.0),
    ([3, 4], 1.0),
    ([4, 0], 0.5000000000000002),
    ([4, 1], 0.5000000000000002),
    ([4, 2], 0.5000000000000002),
    ([4, 3], 0.5000000000000002),
    ([4, 4], 0.5000000000000002)
]

test_mock = [

]


@pytest.mark.parametrize("gens, points, expected", test_solution)
def test_blind_len(gens, points, expected):
    sol = Solution(2, -5, 5, "sphere")
    res = sol.test_blind(gens, points)

    assert len(res) == expected


@pytest.mark.parametrize("gens, points, expected", test_values)
def test_blind_vals(gens, points, expected):
    sol = Solution(2, -5, 5, "sphere")
    res = sol.test_blind(gens, points)

    assert res == expected


@pytest.mark.parametrize("lst, expected", test_levy)
def test_levy(lst, expected):
    functions = Functions("levy")

    assert functions.start(lst) == expected

def call_slow():
    return expensive_call()

def test_mock(mocker):
    mocker.patch(
        # api_call is from slow.py but imported to main.py
        'slow.expensive_call',
        return_value=5
    )

    expected = 5
    actual = call_slow()
    assert actual == expected
    