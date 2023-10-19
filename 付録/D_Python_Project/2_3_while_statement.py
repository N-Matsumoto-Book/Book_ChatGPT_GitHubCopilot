i = 1
while i <= 5:
    print(i)  # 1, 2, 3, 4, 5
    i += 1

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # countが偶数の場合
        continue  # 残りのループをスキップして次のイテレーションに進みます
    print(count)  # 1, 3, 5, 7, 9

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:  # countが5以上になったとき、ループから抜け出す
        break
