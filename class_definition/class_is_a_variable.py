class Money:
    def print_hello(self):
        print('hello')

print(Money.__name__)
print(id(Money))
x = Money
print(x)
print(id(x))
print(x.__name__)
Money = 123
print(id(Money))
print(id(x))
one = x()
one.print_hello()


# one = Money()
# print(one.__class__)