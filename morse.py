num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

code = [i for i in input()]

result = [num[digit.index(each)] for each in code]
print(result)