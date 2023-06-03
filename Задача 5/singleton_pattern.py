import threading
import numpy as np


class SingletonMeta(type):
    """Создание метакласса для реализации шаблона Singleton."""
    # Этот словарь будет содержать экземпляры Singleton классов
    _instances = {}
    # Блокировка, используемая для синхронизации потоков при первом доступе к экземпляру Singleton класса
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Захват блокировки для безопасности потоков
        with cls._lock:
            # Если экземпляр Singleton класса Logger еще не существует, создать его
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        # Вернуть экземпляр Singleton класса
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        """Открывает файл для записи логов"""
        self.file = open("logs/log.txt", "w")

    def write_log(self, thread_name, i, j, val):
        """
        Записывает лог в файл.
        thread_name - имя потока, выполняющего вычисление,
        i, j - индексы элемента матрицы,
        val - вычисленное значение элемента матрицы.
        """
        self.file.write(f"Поток {thread_name} вычислил result[{i}][{j}] = {val}\n")

    def close_log(self):
        """Закрывает файл с логами"""
        self.file.close()


def multiply_matrices(matrix1, matrix2, matrix3, i, j):
    """Выполняет умножение i-й строки матрицы A на j-й столбец матрицы B и сохраняет результат в матрице result"""
    global logger
    matrix3[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(matrix1.shape[1]))
    # Записывает результат в лог
    logger.write_log(threading.current_thread().name, i, j, matrix3[i][j])


def run_threaded_matrix_multiplication(matrix1, matrix2):
    """Создает потоки для умножения строк на столбцы матриц и управляет их выполнением"""
    global logger
    logger = Logger()
    N = matrix1.shape[0]
    # Создаем результирующую нулевую матрицу С размера N x N:
    result_matrix = np.zeros((N, N), dtype=int)

    threads = []
    for i in range(N):
        for j in range(N):
            thread = threading.Thread(target=multiply_matrices, args=(matrix1, matrix2, result_matrix, i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    logger.close_log()
    return result_matrix


if __name__ == "__main__":
    # Тестовый пример многопоточного умножения матриц
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = run_threaded_matrix_multiplication(A, B).tolist()
    print("Результат умножения матриц: \n", " ".join(str(x) for x in result[0]), "\n", " ".join(str(x) for x in result[1]))

