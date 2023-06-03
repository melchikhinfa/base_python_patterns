### Описание шаблона в проекте

Шаблонный метод используется для определения основных шагов алгоритма работы с матрицами в классе AbstractMatrixOperation: загрузка данных, выполнение операции и запись данных. При этом конкретные операции определены в подклассах TransposeMatrix, SumMatrix и DetMatrix. Каждый из них переопределяет метод operation, реализуя конкретную операцию над матрицей.

В функции main выбирается и создается объект нужной операции в зависимости от переданного параметра. Затем вызывается метод execute, который выполняет загрузку данных, операцию над матрицей и запись результатов в файл.

### Диаграмма классов

Диаграмму классов можно нарисовать следующим образом:

AbstractMatrixOperation
    load_data(input_filename)

    write_data(output_filename, data)

    execute(input_filename, output_filename)

    operation(data)

        TransposeMatrix
            operation(data)
        SumMatrix
            operation(data)
        DetMatrix
            operation(data)
