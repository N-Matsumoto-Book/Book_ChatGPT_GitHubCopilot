def print_hello():
    print('hello')


print_hello()  # hello

# print_hello() # NameError
# def print_hello():
#     print('hello')


def print_profile(name, age):
    print(f'name: {name}')
    print(f'age: {age}')


print_profile('Taro', 21)  # name: Taro   age: 21が表示される
print_profile('Hanako', 17)  # name: Hanako   age: 17が表示される


def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # 8


def print_name(name):
    if name == "":
        print("No name")
        return
    print(name)


print_name("Taro")  # Taro
print_name("")  # No name
