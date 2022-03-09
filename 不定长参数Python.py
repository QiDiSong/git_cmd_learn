def fun(*args):
    print("有{}个参数.".format(len(args)))
    print("第2个参数是：{}".format(args[1]))
    print("参数分别为：{}".format(args))
    print()

def fun2(*args, a, b):
    print(args, a, b)


if __name__ == '__main__':
    # fun(1)
    fun(1, 2)
    fun(1, 2, 3)
    print(fun(1, 2, 3, 4))

    # fun2(1, 2, 3, 4, 5)     # fun2() missing 2 required keyword-only arguments: 'a' and 'b'
    fun2(1, 2, 3, a=4, b=5)