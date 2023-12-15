import re


def use_case():
    string = 'Привет! Как дела? У меня все в идеале.'
    result = re.findall(r'\b[бвгджзклмнпрстфхчшщБВГДЖЗКЛМНПРСТФХЧШЩ]\w*', string)
    # берем все слова, начинающиеся на согласную
    print(result)


def print_result(pattern, string):
    result = re.findall(pattern, string)
    print(result)
    print()


def main():
    print('Regex templates')
    hard_string = '87+684645    --- kjgdsklfb98798790909^7 HKLJHLKJHffffggg'

    # в r-строках отключаются специальные символы, к примеру \n

    pattern = r'k.g'  # любой символ, кроме \n
    print_result(pattern, hard_string)

    pattern = r'\d'  # любая цифра
    print_result(pattern, hard_string)

    pattern = r'\D'  # любой символ, но не цифра
    print_result(pattern, hard_string)

    pattern = r'\s'  # любой пробельный символ
    print_result(pattern, hard_string)

    pattern = r'\S'  # любой не пробельный символ (в дальнейшем буду упускать большую букву)
    print_result(pattern, hard_string)

    pattern = r'\w'  # любая буква, цифра или нижнее подчеркивание
    print_result(pattern, hard_string)

    pattern = r'\bHKL'  # начало любого слова
    print_result(pattern, hard_string)
    pattern = r'ffffggg\b'  # конец любого слова
    print_result(pattern, hard_string)

    pattern = r'\d*'  # ноль или более вхождение цифр (*) после цифры (*).
    print_result(pattern, hard_string)

    pattern = r'\d+'  # одно или более вхождение цифр(*) после цифры (*)
    print_result(pattern, hard_string)

    # * - необязательно цифры, зависит от шаблона перед *

    pattern = r'[ghkjd]'  # любые буквы из []
    print_result(pattern, hard_string)
    pattern = r'[4-8]'  # любые цифры из диапазона 4-8 (включительно)
    print_result(pattern, hard_string)
    pattern = r'[^4-8]'  # любые символы НЕ из диапазона 4-8 (включительно)
    print_result(pattern, hard_string)

    pattern = r'H|f'  # или H, или f
    print_result(pattern, hard_string)

    # квантификаторы

    pattern = r'\d{3}'  # = r'\d\d\d'
    print_result(pattern, hard_string)

    pattern = r'\d{1,3}'  # от 1 до 3 (включительно) элементов подходящих под шаблон перед квантификатором
    print_result(pattern, hard_string)

    pattern = r'\d{4,}'  # от 1 элементов подходящих под шаблон перед квантификатором
    print_result(pattern, hard_string)

    pattern = r'\d{4}'  # не более 4 элементов подходящих под шаблон перед квантификатором
    print_result(pattern, hard_string)


if __name__ == '__main__':
    use_case()
