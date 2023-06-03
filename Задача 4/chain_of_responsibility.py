from abc import ABC, abstractmethod
import os
import shutil


class Handler(ABC):
    """Абстрактный класс для обработчиков файлов"""
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        """Устанавливает следующий обработчик в цепочке"""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, file, output_dir):
        """Метод для обработки файла. Если обработчик не может обработать файл, он передает его следующему обработчику."""
        pass

    def _handle_next(self, file, output_dir):
        """Метод для передачи файла следующему обработчику"""
        if self._next_handler:
            return self._next_handler.handle(file, output_dir)


class XmlHandler(Handler):
    """Обработчик XML файлов"""

    def handle(self, file, output_dir):
        if file.endswith(".xml"):
            print(f"Обработчик XML получил файл: {file}")
            shutil.copy(file, os.path.join(output_dir, os.path.basename(file)))
        else:
            return self._handle_next(file, output_dir)


class JsonHandler(Handler):
    """Обработчик JSON файлов"""

    def handle(self, file, output_dir):
        if file.endswith(".json"):
            print(f"Обработчик JSON получил файл: {file}")
            shutil.copy(file, os.path.join(output_dir, os.path.basename(file)))
        else:
            return self._handle_next(file, output_dir)


class CsvHandler(Handler):
    """Обработчик CSV файлов"""
    def handle(self, file, output_dir):
        if file.endswith(".csv"):
            print(f"Обработчик CSV получил файл: {file}")
            shutil.copy(file, os.path.join(output_dir, os.path.basename(file)))
        else:
            return self._handle_next(file, output_dir)


class TxtHandler(Handler):
    """Обработчик TXT файлов"""

    def handle(self, file, output_dir):
        if file.endswith(".txt"):
            print(f"Обработчик TXT получил файл: {file}")
            shutil.copy(file, os.path.join(output_dir, os.path.basename(file)))
        else:
            return self._handle_next(file, output_dir)


class FileParser:
    """Класс для обработки файлов"""
    def __init__(self, handlers):
        """Принимает на вход начальный обработчик в цепочке обработчиков"""
        self.handlers = handlers

    def process(self, file_list, output_dir):
        """Процесс обработки файла. Принимает на вход список файлов и выходную директорию."""
        for file in file_list:
            self.handlers.handle(file, output_dir)


if __name__ == "__main__":
    # Путь до папки с файлами
    files_dir = "data_input"
    files = [os.path.join(files_dir, f) for f in os.listdir(files_dir)]

    # Путь до выходной папки
    output_dir = "data_output"

    # Создаем папку если не существует
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Создание цепочки обработчиков
    handlers = XmlHandler()
    handlers.set_next(JsonHandler()).set_next(CsvHandler()).set_next(TxtHandler())

    # Создание парсера и обработка файлов
    parser = FileParser(handlers)
    parser.process(files, output_dir)
