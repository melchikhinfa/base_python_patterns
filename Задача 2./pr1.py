import numpy as np
import sys

class SumMatrix:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def sum_matrices(self, matrix1, matrix2):
        return np.add(matrix1, matrix2)


    def read_matrices(self, filename):
        with open(filename, 'r') as f:
            matrices = f.read().split('\n\n')
            data = [np.array([list(map(int, row.split())) for row in matrix.split('\n') if row]) for matrix in matrices if matrix]
        return data


    def write_matrix(self, matrix, filename):
        with open(filename, 'a') as f:
            f.write('\n')
            for row in matrix:
                f.write(' '.join(map(str, row)))
                f.write('\n')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = "data/f0.txt"
        output_file = "data/f1.txt"
    summarizer = SumMatrix(input_file, output_file)
    data = summarizer.read_matrices(input_file)
    result_matrix = summarizer.sum_matrices(data[0], data[1])
    summarizer.write_matrix(result_matrix, output_file)
