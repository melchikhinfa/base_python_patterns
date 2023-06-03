import random
import time
from typing import List, Callable


def time_tracker_decorator(sort_algorithm: Callable) -> Callable:
    def wrapper(data: List[int]) -> List[int]:
        start_time = time.time()
        result = sort_algorithm(data)
        end_time = time.time()
        print(f"Сортировка {sort_algorithm.__name__} заняла {end_time - start_time} секунд")
        return result
    return wrapper


@time_tracker_decorator
def selection_sort(data: List[int]) -> List[int]:
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


@time_tracker_decorator
def insertion_sort(data: List[int]) -> List[int]:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


@time_tracker_decorator
def merge_sort(data: List[int]) -> List[int]:
    total_time = 0
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
    return data


def generate_data(n: int) -> List[int]:
    return random.sample(range(n * 10), n)


def write_to_file(file_name: str, sort_type: str, data: List[int]) -> None:
    with open(file_name, "w") as f:
        f.write(f"Тип сортировки: {sort_type}\n")
        f.write(f"Результаты: {', '.join(map(str, data))}\n")


def main(sort_type: str, input_file: str, output_file: str):
    with open(input_file, "r") as f:
        data = list(map(int, f.read().split()))

    if sort_type == "выбором":
        result = selection_sort(data)
    elif sort_type == "вставки":
        result = insertion_sort(data)
    elif sort_type == "слиянием":
        result = merge_sort(data)
    else:
        print("Неизвестный тип сортировки")
        return

    write_to_file(output_file, sort_type, result)


if __name__ == "__main__":
    # Для тестирования программа генерирует файл с исходными данными
    with open("data/input.txt", "w") as f:
        f.write(" ".join(map(str, generate_data(50))))

    # Запускаем программу с каждым типом сортировки
    for sort_type in ["выбором", "вставки", "слиянием"]:
        main(sort_type, "data/input.txt", f"output_{sort_type}.txt")
