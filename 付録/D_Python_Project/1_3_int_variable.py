age = 12
print(type(age))  # <class 'int'>
print(age)  # 12

a = 7
b = 3
print(a + b)  # 加算: 10(7 + 3)
print(a - b)  # 減算: 4(7 - 3)
print(a * b)  # 乗算: 21(7 ✖️3)
print(a // b)  # 整数除算: 2(7 / 3で小数点以下は切り捨てられます)
print(a % b)  # 余り: 1(7 / 3の余り)
print(a ** b)  # べき乗: 343(7の3乗)

height = 175.5
print(type(height))  # <class 'float'>
print(height)  # 175.5

a = 12.5
b = 3.5

print("加算:", a + b)  # 加算: 16.0
print("減算:", a - b)  # 減算: 9.0
print("乗算:", a * b)  # 乗算: 43.75
print("除算（整数除算）:", a // b)  # 除算（整数除算）: 3.0
print("余り:", a % b)  # 余り: 2.0
print("べき乗:", a ** b)  # べき乗: 6905.339660024878

division = a / b
print("除算:", division)  # 除算: 3.5714285714285716

x = 5
x += 3
print(x)  # 8
x -= 2
print(x)  # 6
x *= 3
print(x)  # 18
