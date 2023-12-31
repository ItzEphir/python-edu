from functools import reduce


def main():
    print('Map, Filter, Reduce, Zip')
    example_list = '1 2 3 4 5 6 7 8 9 10'.split()

    # в map передается первым параметром функция, которая применяется к каждому элементу,
    # а вторым аргументом - последовательность, возвращает map
    mapped_list = list(map(int, example_list))
    print(mapped_list)

    # в filter первым параметром передается функция, которая берет каждый аргумент и возвращает bool,
    # а вторым аргуметом - последовательность
    filtered_list = list(filter(lambda x: x % 2 == 0, mapped_list))
    print(filtered_list)

    # в reduce первым параметром передается функция
    # с двумя параметрами - промежуточным результатом и текущим элементом,
    # второй аргумент - последовательность, возвращает совокупное пременение функции к каждому элементу
    print(reduce(lambda result, elem: result * elem, mapped_list))

    # в zip параметрами является перечисляемые,
    # возвращает кортежи со значениями на соответствующих индексах всех перечисляемых
    first_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    second_iterable = 'abcdefghij'
    result = zip(first_iterable, second_iterable)
    print(list(result))
    print(dict(result))  # очень удобно сворачивать два списка в словарь (работает только при двух перечисляемых)
    # почему-то при обороте сначала в list, потом в словарь работать отказывается, при удалении строчки с листом все ок
    print()


if __name__ == '__main__':
    main()
