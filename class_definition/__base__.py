class Person:
    x = 1
    def __init__(self):
        self.x += 10

print(Person.__base__)      # 继承自object， 即为新式类

p = Person()
print(p.x)
print(id(p.x))
print(id(Person.x))
p.x = 20
print(id(p.x))