import numpy as np
import os


def generate_matrices(size):
    matrix1 = np.random.randint(100, size=(size, size))
    matrix2 = np.random.randint(100, size=(size, size))
    return matrix1, matrix2


def write_matrices(matrix1, matrix2, filename):
    with open(filename, 'a') as f:
        f.write('\n\n')
        for row in matrix1:
            f.write(' '.join(map(str, row)) + '\n')
        f.write('\n\n')
        for row in matrix2:
            f.write(' '.join(map(str, row)) + '\n')


def call_p1(input_file, output_file):
    os.system(f"python pr1.py {input_file} {output_file}")


if __name__ == "__main__":
    input_file = "data/f2.txt"
    output_file = "data/f1.txt"

    matrix1, matrix2 = generate_matrices(3)
    write_matrices(matrix1, matrix2, input_file)

    call_p1(input_file, output_file)
