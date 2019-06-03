import pytest

from utils import Fibo


class TestFibbonacci:
    def test_fibo_zero(self):
        assert Fibo.generatefibonacci(0) == 0

    def test_fibo_first(self):
        assert Fibo.generatefibonacci(1) == 1

    def test_fibo_second(self):
        assert Fibo.generatefibonacci(2) == 1

    def test_fibo_oneHundred(self):
        assert Fibo.generatefibonacci(100) == 354224848179261915075

    @pytest.mark.flaky(reruns=5)
    def test_random_rerun(self):
        import random
        assert random.choice([1, 2]) == 2
