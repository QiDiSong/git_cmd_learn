class Animal:
    _x = 10
    def test(self):
        print(self._x)
        print(Animal._x)

class Dog(Animal):
    def test2(self):
        print(Animal._x)
        print(self._x)

a = Animal()
# a.test()

d = Dog()
# d.test2()

print(Animal._x)
print(Dog._x)
print(a._x)
print(d._x)