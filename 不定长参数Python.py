def fun(*args):
    print("有{}个参数.".format(len(args)))
    print("第2个参数是：{}".format(args[1]))
    print("参数分别为：{}".format(args))
    print()

def fun2(*args, a, b):
    print(args, a, b)

def fun3(**kwargs):
    print(kwargs)

def FreeFun(a, *b, **c):
    print(a, b, c)


if __name__ == '__main__':
    # fun(1)
    fun(1, 2)
    fun(1, 2, 3)
    print(fun(1, 2, 3, 4))

    # fun2(1, 2, 3, 4, 5)     # fun2() missing 2 required keyword-only arguments: 'a' and 'b'
    fun2(1, 2, 3, a=4, b=5)

    fun3(a = 6, b = 7, c = 8)       # 将a b c 这种关键字参数转为字典 {'a': 6, 'b': 7, 'c': 8}

    FreeFun(1, 2, 3, 4, x=5, y=6)   # 位置参数必须在关键字参数前面


    ## 解包参数
    def debagParam(a, b, c, d):
        print('debagging:' , a, b, c, d)

    args = (1, 2, 3, 4)
    # debagParam(args)    ##  TypeError: debagParam() missing 3 required positional arguments: 'b', 'c', and 'd'
    debagParam(*args)           # 解包的第一种方式，通过元祖加包解包
    kwargs = {'a':1, 'b':2, 'c':3, 'd':4}
    debagParam(**kwargs)        # 解包的第二种方式，通过字典加包解包