def funA():
    x = 100
    def funB():
        print(x)
    funB()

def funA1():
    x = 100
    def funB1():
        print(x)
    return funB1

## instance
def exp(exp):
    def exp_of(base):
        return base ** exp
    return exp_of


if __name__ == '__main__':
    funA()
    print(funA1())
    funA1()()           ##  funA1() == funB1, 所以 funA1()()等价于funB1()
    funny = funA1()
    funny()             ## 在这里通过闭包实现了访问已经失去作用域的x值（100），这就是闭包

    ## 外层函数的作用域通过某种函数的形式保存下来，尽管这个函数已经调用完毕
    ## 但是外层函数作用于里面的变量，被保存了下来
    ## 并不会像局部作用域那样，调用完就消失了
    ## 也称作工厂函数，实现来料加工，批量生产的功能
    ## 利用嵌套函数实现这个工厂的功能   利用嵌套函数的外层作用于被保存下来的特性 实现批量生产的功能
    square = power(2)
    cube = power(3)
    print(square(5))        # square(5) = 5 * 5 = 25
    print(cube(5))          # cube(5) = 5 * 5 * 5 = 125