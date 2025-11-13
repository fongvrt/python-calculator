import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    #case 1:
    #1. 
    def test_add_0(self):
        self.assertEqual(self.calc.add(0,5),5)
    #2.
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,2),1)
    #case 2:
    #1.
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5,2),3)
    #2.
    def test_negative_result(self):
        self.assertEqual(self.calc.subtract(2,5),-3)
    #case 3.
    #1.
    def test_multiply_by_0(self):
        self.assertEqual(self.calc.multiply(10,0),0)
    #2.
    def test_multiply_by_negative(self):
        self.assertEqual(self.calc.multiply(-10,1),-10)
    #case 4.
    #1.
    def test_devide_by_remainder(self):
        self.assertEqual(self.calc.divide(10,3),3)
    #2.
    def test_devide_by_self(self):
        self.assertEqual(self.calc.divide(9,9),1)
    #case 5.
    #1.
    def test_modulo_default(self):
        self.assertEqual(self.calc.modulo(5,2),1)
    #2.
    def test_modulo_resultisZero(self):
        self.assertEqual(self.calc.modulo(4,2),0)
if __name__ == '__main__':
    unittest.main()