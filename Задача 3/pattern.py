import numpy as np


class AbstractMatrixOperation:
    """Абстрактный класс - шаблон матричных операций"""
    def load_data(self, input_filename):
        """Загрузка данных из файла"""
        with open(input_filename, 'r') as f:
            matrices = f.read().split('\n\n')
            data = [np.array([list(map(int, row.split())) for row in matrix.split('\n') if row]) for matrix in matrices
                    if matrix]
        return data

    def write_data(self, output_filename, data):
        """Запись результата в выходной файл"""
        with open(output_filename, 'a') as f:
            if isinstance(data, np.ndarray):
                for line in data:
                    f.write(' '.join(map(str, line)) + '\n')
                f.write('\n')
            else:
                f.write(str(data) + '\n')

    def execute(self, input_filename, output_filename):
        """Команда выполнения операции"""
        data = self.load_data(input_filename)
        result = self.operation(data)
        self.write_data(output_filename, result)

    def operation(self, data):
        pass


class TransposeMatrix(AbstractMatrixOperation):
    """Операция: транспонирования матрицы"""
    def operation(self, data):
        return data[0].transpose()


class SumMatrix(AbstractMatrixOperation):
    """Операция: сложение матриц"""
    def operation(self, data):
        matrix1, matrix2, _ = data
        return np.add(matrix1, matrix2)


class DetMatrix(AbstractMatrixOperation):
    """Операция: определитель матрицы"""
    def operation(self, data):
        if isinstance(data, list):
            data = data[2]
        if data.shape[0] != data.shape[1]:
            raise ValueError("Матрица должна быть квадратной!")
        return np.linalg.det(data)


def main(op_type, input_filename, output_filename):
    operations = {
        'transpose': TransposeMatrix,
        'sum': SumMatrix,
        'det': DetMatrix
    }

    operation = operations[op_type]()
    operation.execute(input_filename, output_filename)


if __name__ == "__main__":
    main('transpose', 'data/input.txt', 'data/output.txt')
    main('sum', 'data/input.txt', 'data/output.txt')
    main('det', 'data/input.txt', 'data/output.txt')
