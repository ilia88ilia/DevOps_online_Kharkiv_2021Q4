
import unittest
import square_equation

class MyTest(unittest.TestCase):

    def test_discriminant(self):
        self.assertEqual(square_equation.discriminant(-777, -333, 888), 2870793)

    def test_roots(self):
        self.assertEqual(square_equation.roots(2870793, -777, -333, 888), (-1.3045955373195535, 0.8760241087481249))

if __name__ == '__main__':
    unittest.main()