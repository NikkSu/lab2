##Напишите функцию для вывода всех простых чисел в заданном диапазоне
norm_data = []
def is_norm(n):
    if n<=2:
        return False
    for el in range(2, int(n/2)+1):
        if n % el == 0 :
            return False

    return True
def norm_input (n):
    try:
       value = int(input(n))
       if value <= 0: print ("значение должно быть больше 0")
       else:
           return value
    except ValueError:
        print ("число ввести надо")
def progon():
    start = norm_input("введите начало диапазона ")
    end = norm_input("введите конец диапазона ")
    for el in range (start, end+1):
        if is_norm(el):
               norm_data.append(el)
    print ("норм числа: ",norm_data)

progon()