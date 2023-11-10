#Найти в матрице первый столбец, все элементы которого отрицательны, и среднее арифметическое этих элементов
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
while True:
    rows = input("Введите количество строк в матрице: ")
    columns = input("Введите количество столбцов в матрице: ")
    if not rows.isdigit() or not columns.isdigit():
        print("Некорректный ввод. Введите целые числа.")
    else:
        rows = int(rows)
        columns = int(columns)
        break
matrix = []
#i - строка, j - столбец
for i in range(rows):
    row = []
    for j in range(columns):
        while True:
            value = input(f"Введите элемент [{i}][{j}]: ")
            if not is_float(value):
                print("Некорректный ввод. Введите число.")
            else:
                row.append(float(value))
                break
    matrix.append(row)
column_index = -1
for j in range(columns):
    all_negative = True
    for i in range(rows):
        if matrix[i][j] >= 0:
            all_negative = False
            break
    if all_negative:
        column_index = j
        break

if column_index != -1:
    column_values = [matrix[i][column_index] for i in range(rows)]
    average = sum(column_values) / len(column_values)
    print(f"Среднее арифметическое элементов столбца {column_index}: {average}")
else:
    print("В матрице нет столбца, все элементы которого отрицательны.")