import pytest


class TestRerun:

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_random_rerun(self):
        import random
        assert random.choice([1, 2]) == 2