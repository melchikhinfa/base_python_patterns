from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Абстрактный класс фабрики, определяющий общий интерфейс для создания сортировки.
    Все конкретные фабрики должны следовать этому интерфейсу.
    """

    @abstractmethod
    def create_sort(self):
        """
        Абстрактный метод для создания конкретного алгоритма сортировки.
        """
        pass

class SelectionSortFactory(AbstractFactory):
    """
        Конкретная фабрика для создания продукта - алгоритма сортировки выбором.
    """
    def create_sort(self):
        return SelectionSort()


class InsertionSortFactory(AbstractFactory):
    """
        Конкретная фабрика для создания продукта - алгоритма сортировки вставками.
    """
    def create_sort(self):
        return InsertionSort()


class MergeSortFactory(AbstractFactory):
    """
       Конкретная фабрика для создания продукта - алгоритма сортировки слиянием.
    """
    def create_sort(self):
        return MergeSort()


class AbstractSort:
    """Kласс, который содержит общий интерфейс для всех сортировок"""
    def sort(self, data):
        pass


class SelectionSort(AbstractSort):
    def sort(self, data):
        for i in range(len(data)):
            # Ищем минимальный элемент в оставшейся части массива
            min_index = i
            for j in range(i + 1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j

            # Меняем местами найденный минимальный элемент и первый в оставшейся части массива
            data[i], data[min_index] = data[min_index], data[i]

        return data


class InsertionSort(AbstractSort):
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]

            # Смещаем элементы массива data[0..i-1], которые больше, чем key, на одну позицию вперед
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

        return data


class MergeSort(AbstractSort):
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self, data):
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        left = self.sort(left)
        right = self.sort(right)

        return self.merge(left, right)


def read_data_from_file(filename):
    # функция для чтения данных из файла
    with open(filename, 'r') as file:
        data = file.readline()
        return list(map(int, data.split(' ')))  # преобразуем строки в числа


def write_data_to_file(filename, sort_type, output_data):
    # функция для записи отсортированных данных и типа сортировки в файл
    with open(filename, 'a') as file:
        file.write(f"Тип сортировки: {sort_type}\n")
        file.write(','.join(map(str, output_data)) + '\n\n')  # преобразуем числа обратно в строки для записи


def main(sort_type, input_filename, output_filename):
    factories = {
        'selection': SelectionSortFactory,
        'insertion': InsertionSortFactory,
        'merge': MergeSortFactory
    }

    factory = factories[sort_type]()
    sorting = factory.create_sort()
    data = read_data_from_file(input_filename)
    sorted_data = sorting.sort(data)
    write_data_to_file(output_filename, sort_type, sorted_data)


if __name__ == "__main__":
    inp_file = 'data/input.txt'
    out_file = 'data/output.txt'
    main('merge', inp_file, out_file)
    main('insertion', inp_file, out_file)
    main('selection', inp_file, out_file)

