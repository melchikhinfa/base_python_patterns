class MatrixOps:
    """Базовый класс для матричных операций."""
    def perform_operation(self, matrices):
        """Метод для выполнения матричной операции."""
        pass


class MatrixMultiply(MatrixOps):
    """Класс для выполнения операции умножения матриц."""
    def perform_operation(self, matrices):
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrices[1])] for X_row in matrices[0]]
        return result


class MatrixAdd(MatrixOps):
    """Класс для выполнения операции сложения матриц."""
    def perform_operation(self, matrices):
        result = [[matrices[0][i][j] + matrices[1][i][j] for j in range(len(matrices[0][0]))] for i in
                  range(len(matrices[0]))]
        return result


class MatrixTranspose(MatrixOps):
    """Класс для выполнения операции транспонирования матрицы."""
    def perform_operation(self, matrices):
        result = [[matrices[0][j][i] for j in range(len(matrices[0]))] for i in range(len(matrices[0][0]))]
        return result


class MatrixDeterminant(MatrixOps):
    """Класс для выполнения операции вычисления определителя матрицы."""
    def perform_operation(self, matrices):
        return [[self._calculate_determinant(matrices[0])]]

    @staticmethod
    def _calculate_determinant(matrix):
        """Вспомогательный метод для вычисления определителя матрицы."""
        total = 0
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

        for column in range(len(matrix)):
            temp = [row[:column] + row[column + 1:] for row in matrix[1:]]
            sign = (-1) ** column
            sub_det = MatrixDeterminant._calculate_determinant(temp)
            total += sign * matrix[0][column] * sub_det
        return total


class Invoker:
    """Класс, отвечающий за вызов команд."""
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        """Метод для добавления команды."""
        self.commands.append(command)

    def run_commands(self):
        """Метод для выполнения всех команд."""
        for command in self.commands:
            command.execute()


class Command:
    """Базовый класс для команд."""
    def execute(self):
        """Метод для выполнения команды."""
        pass


class ReadCommand(Command):
    """Класс команды для чтения матрицы из файла."""
    def __init__(self, filename):
        self.filename = filename

    def execute(self):
        with open(self.filename, 'r') as file:
            return [list(map(int, line.split())) for line in file]


class WriteCommand(Command):
    """Класс команды для записи матрицы в файл."""
    def __init__(self, filename, matrix):
        self.filename = filename
        self.matrix = matrix

    def execute(self):
        with open(self.filename, 'w') as file:
            file.writelines(' '.join(map(str, row)) + '\n' for row in self.matrix)


class MatrixOpsCommand(Command):
    """Базовый класс для команд, которые выполняют операции над матрицами."""
    def __init__(self, matrices):
        self.matrices = matrices
        self.operation = None

    def execute(self):
        return self.operation.perform_operation(self.matrices)


class MultiplyCommand(MatrixOpsCommand):
    """Класс для команды умножения матриц."""
    def __init__(self, matrices):
        super().__init__(matrices)
        self.operation = MatrixMultiply()


class AddCommand(MatrixOpsCommand):
    """Класс для команды сложения матриц."""
    def __init__(self, matrices):
        super().__init__(matrices)
        self.operation = MatrixAdd()


class TransposeCommand(MatrixOpsCommand):
    """Класс для команды транспонирования матрицы."""
    def __init__(self, matrices):
        super().__init__(matrices)
        self.operation = MatrixTranspose()


class DeterminantCommand(MatrixOpsCommand):
    """Класс для команды вычисления определителя матрицы."""
    def __init__(self, matrices):
        super().__init__(matrices)
        self.operation = MatrixDeterminant()


class RunCommand(Command):
    """Класс для команды выбора и вызова операции над матрицами."""
    def __init__(self, operation, matrices):
        self.operation = operation
        self.matrices = matrices

    def execute(self):
        operations = {
            '*': MultiplyCommand,
            '+': AddCommand,
            't': TransposeCommand,
            'd': DeterminantCommand,
        }
        operation_class = operations.get(self.operation)
        if operation_class:
            return operation_class(self.matrices).execute()
        else:
            print(f"Unknown operation {self.operation}")


def main(operation, input_files, output_file):
    invoker = Invoker()


    for input_file in input_files:
        read_command = ReadCommand(input_file)
        invoker.add_command(read_command)

    matrices = [command.execute() for command in invoker.commands]
    invoker.commands.clear()  # очищаем список команд

    # Добавляем команду выполнения операции
    run_command = RunCommand(operation, matrices)
    invoker.add_command(run_command)
    result = invoker.commands[0].execute()
    invoker.commands.clear()

    # Добавляем команду записи результата
    write_command = WriteCommand(output_file, result)
    invoker.add_command(write_command)

    # Запускаем все команды
    invoker.run_commands()


main('+', ['matrix1.txt', 'matrix2.txt'], 'result.txt')
