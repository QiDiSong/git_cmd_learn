class Person:
    '''
    当我们通过 “实例.属性 = 值”(p.age = 18, 类似于这种)，给一个实例增加或者修改一个属性的时候， 都会调用这个setattr方法
    在这个方法内部，才会真正的把这个属性，以及对应的数据，给存储到__dict__字典里面
    '''
    def __setattr__(self, key, value):
        print(key, value)

        # 1. 判定 key  是否是我们要设置的只读属性
        # 并且该属性之前并不存在于__dict__字典里， 否则就是添加，而不是修改
        if key == 'age' and key in self.__dict__.keys():
            print('这个属性是只读属性，不能修改数据')
        # 2. 如果说不是age，那么只读属性的名称，真正的给他添加到这个实例里面去
        else:
            # self.key = value        # 不能这么写，因为当这么写的时候，就会重新调用setattr方法，陷入死循环中
            self.__dict__['age'] = value


p = Person()
p.age = 18
print(p.age)
print()
p.age = 20
# print(p.age)
print(p.__dict__)