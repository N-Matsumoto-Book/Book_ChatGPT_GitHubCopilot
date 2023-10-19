import random
from random import Random
from math import sqrt as sq, fabs as fa
from math import sqrt, fabs
import math

print(math.sqrt(16))  # 引数の平方根をfloatで取得(4.0)
print(math.fabs(-5))  # 引数の絶対値をfloatで取得(5.0)


print(sqrt(16))  # 引数の平方根をfloatで取得(4.0)
print(fabs(-5))  # 引数の絶対値をfloatで取得(5.0)

print(sq(16))  # 引数の平方根をfloatで取得(4.0)
print(fa(-5))  # 引数の絶対値をfloatで取得(5.0)

rand = Random()  # Randomクラスのインスタンス化
print(rand.randint(0, 10))  # 0から10までのランダムな整数を生成
print(random.randint(0, 10))  # 0から10までのランダムな整数を生成
