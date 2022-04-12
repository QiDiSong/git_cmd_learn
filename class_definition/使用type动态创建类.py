def run(self):
    print('---', self)

myClass = type('Dog', (), {'count': 9, 'run': run})
print(myClass)
print(myClass.__dict__)
print()

me = myClass()
me.run()
print(me)