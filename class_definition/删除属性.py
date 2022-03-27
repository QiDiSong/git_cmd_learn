class Money:
    num = 100
    age = 20
    count = 1


print(Money.num)
del Money.num
# print(Money.num)

m = Money()
# print(m.num)
m.num = 1
print(m.num)
print(m.__dict__)