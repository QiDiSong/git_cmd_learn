class Money:
    age = 1
    num = 2
    count = 0

print(Money.age)
print(Money.num)
print(Money.count)

print(Money.__dict__)

m = Money()
print(m.age)
print(m.num)
print(m.count)
m.sex = 'female'
print(m.__dict__)

class Money_:
    sex = 'male'
print()
print(m.__class__)
m.__class__ = Money_
print(m.sex)

