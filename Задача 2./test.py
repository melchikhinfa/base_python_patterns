import unittest
import os
from pr1 import SumMatrix
import numpy as np



class TestProgramP2(unittest.TestCase):
    def test_program_p2(self):
        input_file = "tests/test_F2.txt"
        output_file = "tests/test_F1.txt"

        matrix1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        matrix2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

        with open(input_file, 'a') as f:
            f.write('\n\n')
            for row in matrix1:
                f.write(' '.join(map(str, row)) + '\n')
            f.write('\n\n')
            for row in matrix2:
                f.write(' '.join(map(str, row)) + '\n')

        os.system(f"python pr1.py {input_file} {output_file}")

        with open(output_file, 'r') as f:
            matrices = f.read().split('\n')
            data = [list(map(int, row.split())) for row in matrices if row]

        expected_output = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.assertEqual(data, expected_output)

    def test_program_p1(self):
        input_file = "tests/test_F0.txt"
        output_file = "tests/test_F1.txt"
        pr1 = SumMatrix(input_file, output_file)

        matrix1_excpected = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
        matrix2_excpected = [[20, 20, 20], [20, 20, 20], [20, 20, 20]]
        expected_output = np.array([[30, 30, 30], [30, 30, 30], [30, 30, 30]]).tolist()

        matrix1 = pr1.read_matrices(input_file)[0]
        self.assertEqual(matrix1.tolist(), matrix1_excpected)

        matrix2 = pr1.read_matrices(input_file)[1]
        self.assertEqual(matrix2.tolist(), matrix2_excpected)

        result = pr1.sum_matrices(matrix1, matrix2).tolist()
        self.assertEqual(result, expected_output)



if __name__ == "__main__":
    unittest.main()
