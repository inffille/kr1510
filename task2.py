def f(x, y):
    return float(x) + float(y)


print('Input numbers')
x = input()
y = input()
print(str(x) + '+' + str(y), '=', f(x, y))