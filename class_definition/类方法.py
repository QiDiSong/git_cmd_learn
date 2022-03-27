class Person:
    def instance(self):
        print('This is a instance method. ', self)

    @classmethod
    def class_(cls):
        print('this is a class method. ', cls)

    @staticmethod
    def static():
        print('this is a static method. ')

p = Person()
p.class_()
p.static()
p.instance()
print(p)


class Money:
    def eat(self, food):
        print(self, food)
    def eat2(xxx, food):
        print(xxx, food)
print()
m = Money()
m.eat('q')
print(m)
Money.eat(m, 'a')

m.eat2('abc')
n = Money()
n.eat('asd')


l = [2, 4, 6, 1, 0]
l.sort()        # 实例方法
sorted(l)       # 静态方法