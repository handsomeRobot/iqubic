#coding=utf-8


#Import necessary modules
import csv
import unittest
import random


#The class of Matrix
class Matrix:
    def __init__(self, array):
        self.array = array
        self.determ = 'NA'
        for n, row in enumerate(self.array):
            if n == 0:
                continue
            else:
                if len(self.array[n - 1]) != len(row):
                    raise ValueError('This is not a matrix.')
    def get_id(self):
        return self.id
    def get_shape(self):
        return(len(self.array), len(self.array[0]))
    def get_array(self):
        return(self.array)
    def __getitem__(self, key):
        return self.array[key]
    def __eq__(self, other):
        #Overrides the default implementation
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False
    #Matrix transverse function
    def get_trans(self):
        m, n = self.get_shape()
        matrix_copy = Matrix([[0 for i in range(m)] for j in range(n)])
        for i in range(n):
            for j in range(m):
                matrix_copy[i][j] = self[j][i]
        return matrix_copy   
    #Matrix copy function(self):
    def get_copy(self):
        m, n = self.get_shape()
        matrix_copy = Matrix([[0 for i in range(n)] for j in range(m)])
        for i in range(m):
            for j in range(n):
                matrix_copy[i][j] = self[i][j]
        return matrix_copy
    #Matrix remainder function
    def get_remainder(self, p, q):
        #python starts from zero :)
        p -= 1
        q -= 1
        m, n = self.get_shape()
        matrix_copy = self.get_copy()
        #Remove the pth row
        array = matrix_copy.get_array()
        array.pop(p)
        #Remove the qth column
        for row in array:
            row.pop(q)
        #Pack the array into a Matrix class again
        return matrix_copy
    #Matrix determinants function
    def get_determ(self):
        m, n = self.get_shape()
        if m != n:
            raise ValueError("Cannot calculate determinant for non-square matrix.")
        if self.determ == 'NA':
            self.determ = 0
        if m > 2:
            for j in range(n):
                remainder = self.get_remainder(1, j + 1)
                self.determ += (-1)**(j) * self[0][j] * remainder.get_determ()
        elif m == 2:
            result = self[0][0] * self[1][1] - self[0][1] * self[1][0]
            return result    
        return self.determ       
    #Matrix multiply function
    def multiply_matrix(self, matrix2):
        m, n = self.get_shape()
        p, q = matrix2.get_shape()
        if n != p:
            raise ValueError("get_shapes of matrixs do not match for multiply.")
        result = Matrix([[0 for i in range(q)] for j in range(m)])
        for i in range(m):
            for k in range(q):
                for j in range(n):
                    result[i][k] += self[i][j] * matrix2[j][k]
        return result


   
class TestMatrixFunc(unittest.TestCase):
    #Test multiply
    def test_matrix_mult(self):
        self.assertEqual(Matrix([[9, 12, 15], [19, 26, 33], [29, 40, 51]]), \
                         Matrix([[1, 2], [3, 4], [5, 6]]).multiply_matrix(Matrix([[1, 2, 3], [4, 5, 6]])))
        self.assertNotEqual(Matrix([[9, 12, 15], [19, 26, 33], [29, 45, 51]]), \
                         Matrix([[1, 2], [3, 4], [5, 6]]).multiply_matrix(Matrix([[1, 2, 3], [4, 5, 6]])))
    #Test transverse
    def test_matrix_trans(self):
        self.assertEqual(Matrix([[1, 3, 5], [2, 4, 6]]), Matrix([[1, 2], [3, 4], [5, 6]]).get_trans())
        self.assertNotEqual(Matrix([[2, 4, 6], [1, 3, 5]]), Matrix([[1, 2], [3, 4], [5, 6]]).get_trans())
    #Test remainder
    def test_matrix_remainder(self):
        self.assertEqual(Matrix([[4, 6], [7, 9]]), Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_remainder(1, 2))
        self.assertEqual(Matrix([[4]]), Matrix([[1, 2], [3, 4]]).get_remainder(1, 1))
        self.assertNotEqual(Matrix([[3, 4]]), Matrix([[1, 2], [3, 4]]).get_remainder(2, 2))
    #Test determinant
    def test_matrix_determ(self):
        self.assertNotEqual(0, Matrix([[2, 3], [9, 11]]).get_determ())
        self.assertEqual(-5, Matrix([[2, 3], [9, 11]]).get_determ())
        self.assertEqual(46, Matrix([[3, 2, 4], [3, 5, 2], [2, 4, 6]]).get_determ())
        self.assertEqual(330, Matrix([[2, 2, 2, 2], [5, 2, 7, 8], [9, 10, 2, 12], [13, 14, 15, 19]]).get_determ())
        self.assertEqual(-96456, Matrix([[2, 2, 2, 2, 8], [5, 2, 7, 8, 100], [9, 10, 2, 12, 11], [13, 14, 15, 19, 10], [10, 2, 3, 4, 1]]).get_determ())

    
if __name__ == '__main__':
    try:
        unittest.main(verbosity = 2)
    except Exception as e:
        print(e)

        