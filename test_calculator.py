"""

Unit test for calculator library
"""
import calculator


class TestCalculator:

    def test_add(self):
        assert 40 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.sub(4, 2)
