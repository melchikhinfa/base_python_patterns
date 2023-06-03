import unittest
import numpy as np
from pattern import AbstractMatrixOperation, TransposeMatrix, SumMatrix, DetMatrix

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.data_to_transponse = np.array([[5, 2, 3], [3, 8, 6], [1, 7, 5]])
        self.data_to_det = np.array([[34, 61, 3], [76, 12, 63], [2, 44, 11]])
        self.data_to_sum = [self.data_to_det, self.data_to_transponse, ""]


    def test_transpose(self):
        transpose_op = TransposeMatrix()
        result = transpose_op.operation([self.data_to_transponse])
        expected = np.array([[5, 3, 1], [2, 8, 7], [3, 6, 5]])
        np.testing.assert_array_equal(result, expected)

    def test_sum(self):
        sum_op = SumMatrix()
        result = sum_op.operation(self.data_to_sum)
        expected = np.array([[39, 63, 6], [79, 20, 69], [3, 51, 16]])
        np.testing.assert_array_equal(result, expected)

    def test_det(self):
        det_op = DetMatrix()
        result = round(det_op.operation(self.data_to_det))
        expected = -123110
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()