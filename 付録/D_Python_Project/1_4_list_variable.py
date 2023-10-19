empty_list = []  # 空のリストを作成
numbers = [1, 2, 3, 4, 5]  # 数値のリストを作成
fruits = ['apple', 'banana', 'orange']  # 文字列のリストを作成
mixed_list = [1, 'two', 3.0, [4, 'four']]  # 異なるデータ型を含むリストを作成

fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange

fruits[1] = 'blueberry'
print(fruits)  # ['apple', 'blueberry', 'orange', 'grape']

fruits = ['apple', 'banana', 'orange']
fruits.append('grape')  # grapeをfruits変数の末尾に格納する
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()  # 昇順に並び替える
print(my_list)  # [1, 1, 2, 3, 4, 5, 6, 9]

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort(reverse=True)  # 降順に並び替える
print(my_list)  # [9, 6, 5, 4, 3, 2, 1, 1] を出力

fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')  # bananaをfruitsから削除
print(fruits)  # ['apple', 'orange', 'banana']

numbers = [1, 2, 3, 4, 5]
first_number = numbers.pop(0)  # リストの最初の要素を取り出す
print(first_number)  # 出力: 1
print(numbers)  # 出力: [2, 3, 4, 5]
