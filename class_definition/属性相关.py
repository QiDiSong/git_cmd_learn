class Person():
    pass

p = Person()

p.age = 18
print(p.age, id(p.age))

p.age = 19
print(p.age, id(p.age))


p.pets = [1, 2]
print(p.pets, id(p.pets))

p.pets = [3, 4]                     # id与上面的[1, 2]相同
print(p.pets, id(p.pets))

p.pets = ['1', '2']                 # 变成字符后，id就会变
print(p.pets, id(p.pets))



