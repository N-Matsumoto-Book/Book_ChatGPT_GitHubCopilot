for num in [1, 2, 3, 4, 5]:
    print(num)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)  # apple, banana, cherryを順に表示する

message = 'Hello'
for character in message:
    print(character)  # H,e,l,l,oが、1文字ずつ表示される


fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
for key in fruits:
    print(key)  # apple, banana, cherry

for num in range(5):
    print(num)

for i in range(5):  # 引数が1つの場合
    print(i)  # 0, 1, 2, 3, 4を順に表示

for i in range(2, 5):  # 引数が2つの場合
    print(i)  # 2, 3, 4を順に表示

for i in range(0, 10, 2):  # 引数が3つの場合
    print(i)  # 0, 2, 4, 6, 8を順に表示

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)  # 1, 2, 4, 5, 7, 8, 10

for i in range(1, 11):
    if i % 3 == 0:
        break
    print(i)  # 1, 2
