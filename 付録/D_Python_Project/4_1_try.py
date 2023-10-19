try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError as e:
    print("エラーが発生しました")
print("ここがプログラムの終了箇所です")


def is_positive(number):
    if number <= 0:  # 引数numberが0以下の場合
        raise ValueError("Error: The number must be positive!")
    print(f"{number} is positive")


# ValueErrorが発生する例
try:
    is_positive(-5)  # ValueErrorが発生
except ValueError as e:
    print(e)  # Error: The number must be positive!

# エラーが発生しない例
try:
    is_positive(10)  # エラーは発生しない
    print("この処理は実行される")
except ValueError as e:
    print(e)  # 実行されない
