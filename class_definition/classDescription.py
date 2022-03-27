class Person:
    """
    Description: 关于这个类的描述可以放在这里，类的作用，类的构造函数等等 ，类属性的描述
    """

    count = 1
    def run(self, distance, step):
        """
        这个方法的作用效果
        :param distance: 参数的含义，参数的类型为int，是否有默认值等
        :param step: step的含义， 参数的类型为int，是否有默认值等
        :return: 返回值是什么，返回的结果的含义（时间），返回数据的类型int
        """
        print('people is running!') 
        return distance // step

help(Person)

def fun():
    '''
    这是一个函数 有xxx作用
    :return: None
    '''