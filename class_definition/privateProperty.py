class Animal:
    __x = 10
    def test(self):
        print(Animal.__x)
        print(self.__x)

'''
用于数据保护和数据私有（私有化属性的应用场景）
'''
print(Animal.__dict__)
print(Animal._Animal__x)
print()


class Person:

    def __init__(self):
        self.__age = 18

    def setAge(self, age):
        if isinstance(age, int) and 0 < age < 200:
            self.__age = age
        else:
            print('你输入的age有误')

    def getAge(self):
        return self.__age

p = Person()
print(p.getAge())
p.setAge(1000)
# print(p.__dict__)
print(p.getAge())