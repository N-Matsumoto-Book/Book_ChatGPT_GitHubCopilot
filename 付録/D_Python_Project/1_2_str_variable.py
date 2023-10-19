msg = 'Hello, World!'
msg = "Hello, World!"

msg1 = "Hello"
msg2 = "World"
result = msg1 + ", " + msg2 + "!"  # (「msg1」と「, 」と「msg2」と「!」の値を結合しています)
print(result)  # Hello, World!

msg1 = "Hello"
msg2 = "World"
result = f"{msg1}, {msg2}!"
print(result)  # Hello, World!

text = "Hello, World!"

index = text.find("World")
print(index)  # 7
index = text.find("Japan")
print(index)  # -1

text = "Hello, World! How are you?"
words1 = text.split(", ")  # カンマで分割する
print(words1)  # ["Hello", "World! How are you?"]
words2 = text.split()  # スペースで分割
print(words2)  # ["Hello,", "World!", "How", "are", "you?"]
