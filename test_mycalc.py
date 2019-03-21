import random

import pytest

import mycalc


def test_add():
    assert mycalc.add(1, 2) == 3


@pytest.mark.skipif(random.random() < 0.5,
                    reason="Умножению не повезло")
def test_mul():
    assert mycalc.mul(3, 7) == 21


def test_sub():
    assert mycalc.sub(4, 2) == 2


def test_div():
    assert mycalc.div(16, 8) == 2
    assert mycalc.div(16, 4) == 4


def test_sqrt():
    assert (mycalc.sqrt(9) - 3) < 0.000000001
    assert (mycalc.sqrt(25) - 5) < 0.000000001
