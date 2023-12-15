
def main():
    # * - генерирует tuple от всех переданных элементов
    def function1(*args):
        print(args)

    function1(1, 2, 3, 4)

    # ** - генерирует dict от именованных значений (ключ - имя)
    def function2(**kwargs):
        print(kwargs)
    function2(a="Cool", b="Text", c="I`m mr.Beast")


if __name__ == '__main__':
    main()

