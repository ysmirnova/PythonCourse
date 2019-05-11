from utils import Fibo


class Testv_Fibbonacci:
    def test_fibo_zero(self):
        assert Fibo.generatefibonacci(0) == 0

    def test_fibo_first(self):
        assert Fibo.generatefibonacci(1) == 1

    def test_fibo_second(self):
        assert Fibo.generatefibonacci(2) == 1

    def test_fibo_oneHundred(self):
        assert Fibo.generatefibonacci(100) == 354224848179261915075
