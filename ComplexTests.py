import unittest
import ComplexLibrary as cpl

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        c1=(-6,-9)
        c2=(-5,8)
        self.assertEqual(cpl.suma(c1, c2), (-11,-1))

if __name__ == '__main__':
    unittest.main()