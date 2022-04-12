class Money:
    pass

Money.age = 1

print(Money.age)
print(Money.__name__)
print(Money.__dict__)

print('age' in Money.__dict__)
print(1 in Money.__dict__)
print('__doc__' in Money.__dict__)

m = Money()
print(m.__dict__)
m.count = 10
print(m.__dict__)
print('count' in m.__dict__)

n = Money()
print('count' in n.__dict__)