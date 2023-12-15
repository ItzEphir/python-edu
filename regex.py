import re


def main():
    string = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

    # метод match ищет в начале строки соответствующий паттерн, если не найдено - None
    result = re.match('AC', string)
    print(result)
    print(result[0])
    print()

    # метод search ищет первое вхождение паттерна в строку, если не найдено - None
    result = re.search('DC', string)
    print(result)
    print(result[0])
    print()

    # метод findall ищет все вхождения паттерна в строку, возвращает список
    result = re.findall('DC', string)
    print(result)
    print()

    # метод split делит строку по заданному паттерну, работает как split, только по паттерну, возвращает список,
    # в параметры можно задать maxsplit, что задает максимальное количество разбиений
    result = re.split('/', string)
    print(result)
    print()

    # метод sub заменяет все вхождения паттерна на другую строку, возвращает строку
    result = re.sub('A', 'U', string)
    print(result)
    print()

    # метод fullmatch работает как match, только проверяет, совпадает ли вся строка под паттерн, если нет - None
    result = re.fullmatch('AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC', string)
    print(result)
    result = re.fullmatch('A', string)
    print(result)
    print()


if __name__ == '__main__':
    main()
