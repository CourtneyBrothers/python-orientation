import unittest
import calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.calculator = calculator.Calculator()
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calculator.add(2, 7), 9)
    self.assertEqual(self.calculator.subtract(7,2),5)
    self.assertEqual(self.calculator.multiply(3,5),15)
    self.assertEqual(self.calculator.divide(15,5),3)

  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()

