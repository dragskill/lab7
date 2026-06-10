import unittest
from main import objective_function, gradient_function

class TestGradientDescent(unittest.TestCase):
    def test_objective_function(self):
        self.assertEqual(objective_function(2), 0)

    def test_gradient_function(self):
        self.assertEqual(gradient_function(2), 0)

if __name__ == '__main__':
    unittest.main()