### Описание шаблона в проекте
Абстрактная фабрика используется для создания одного из трех типов сортировки (выбором, вставками, слиянием) в зависимости от переданного параметра. Все три типа сортировки являются продуктами и реализуют интерфейс AbstractSort, который определяет метод sort.

В функции main создается экземпляр фабрики в зависимости от переданного типа сортировки. Затем с помощью этой фабрики создается объект сортировки. Данные для сортировки считываются из файла, сортируются, и отсортированные данные записываются в другой файл.

### Диаграмма классов
Диаграмму классов можно нарисовать следующим образом:

AbstractSortFactory
    create_sort()
        SelectionSortFactory
            create_sort()
        InsertionSortFactory
            create_sort()
        MergeSortFactory
            create_sort()

AbstractSort
    sort(data)
        SelectionSort
            sort(data)
        InsertionSort
            sort(data)
        MergeSort
            sort(data)