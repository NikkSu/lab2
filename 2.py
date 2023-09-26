##Напишите функцию, которая будет принимать один аргумент. Если в
##функцию передаётся список, Найдите произведение элементов с нечетными
##номерами. Найдите наибольший элемент списка, затем удалите его и
##выведите новый список.
##Если словарь, вывести на экран первые три наибольших значения.
##Число – определить сумму его цифр.
##Строка – определить сколько в ней гласных, а сколько согласных. Посчитать количество слов.
def process_list(data):
    product_odd_indices = 1
    for i, value in enumerate(data):
        if i % 2 != 0:
            product_odd_indices *= value
    print("Произведение элементов с нечетными индексами:", product_odd_indices)

    max_value = max(data)
    data.remove(max_value)
    print("Новый список после удаления наибольшего элемента:", data)


def process_dict(data):
    sorted_values = sorted(data.values(), reverse=True)
    top_three_values = sorted_values[:3]
    print("Первые три наибольших значения в словаре:", top_three_values)


def process_number(data):
    digits_sum = sum(int(digit) for digit in str(data))
    print("Сумма цифр числа:", digits_sum)


def process_string(data):
    vowels = 0
    consonants = 0
    for char in data:
        if char.lower() in "aeiouy":
            vowels += 1
        elif char.isalpha():
            consonants += 1
    print("Количество гласных:", vowels)
    print("Количество согласных:", consonants)

    words = data.split()
    num_words = len(words)
    print("Количество слов:", num_words)


def process_data(data):
    if isinstance(data, list):
        process_list(data)
    elif isinstance(data, dict):
        process_dict(data)
    elif isinstance(data, int):
        process_number(data)
    elif isinstance(data, str):
        process_string(data)
    else:
        print("Неподдерживаемый тип данных.")


def get_user_input():
    user_input = input("Введите данные: ")
    return user_input


def main():
    user_input = get_user_input()

    try:
        processed_data = None

        if user_input.isdigit():
            processed_data = int(user_input)
        elif user_input.startswith('[') and user_input.endswith(']'):
            processed_data = eval(user_input)
        elif user_input.startswith('{') and user_input.endswith('}'):
            processed_data = eval(user_input)
        else:
            processed_data = user_input

        process_data(processed_data)
    except (NameError, SyntaxError):
        print("Ошибка: некорректный ввод.")
    except Exception as e:
        print("Произошла ошибка:", str(e))
    finally:    print ("finally ")


if __name__ == "__main__":
    main()