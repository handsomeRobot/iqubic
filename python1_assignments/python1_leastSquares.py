#coding=utf-8

import unittest



def least_squares(ls1, ls2):
    if len(ls1) != len(ls2):
        raise ValueError('Comparing lists do not have the same length.')
    result = 0
    for n, i in enumerate(ls1):
        diff = float(ls1[n] - ls2[n])
        result += diff ** 2
    return result
    
    
    
class TestMatrixFunc(unittest.TestCase):
    #test least_squares
    def test_least_square(self):
        self.assertEqual(0, least_squares([1, 2], [1, 2]))
        self.assertNotEqual(0, least_squares([1, 3, 5], [4, 2, 5]))
        

if __name__ == '__main__':
    unittest.main(verbosity = 2)        