##Напишите функцию для вывода всех простых чисел в заданном диапазоне
def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def get_valid_input(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Введенное значение должно быть числом больше 0.")
            else:
                return value
        except ValueError:
            print("Введенное значение должно быть числом.")
def print_prime_numbers():
    start = get_valid_input("Введите начало диапазона: ")
    end = get_valid_input("Введите конец диапазона: ")

    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    print(f"Простые числа в диапазоне [{start}, {end}]: {prime_numbers}")


print_prime_numbers()