class Sample:
    def print_hello(self):  # インスタンスメソッド
        print("Hello")


my_sample = Sample()  # インスタンス作成
my_sample.print_hello()  # Hello
# Sample.print_hello() # エラー


class Sample_2:
    @classmethod
    def print_hello(cls):  # クラスメソッド
        print("Hello")


Sample_2.print_hello()  # Hello


class User:
    user_infos = {"Alice": "Programmer", "Bob": "Data Scientist"}

    @classmethod
    def get_profession(cls, name):
        return cls.user_infos.get(name)

    @classmethod
    def print_user_info(cls, name):
        # clsを使って、クラスメソッドget_professionを実行
        profession = cls.get_profession(name)
        if profession:
            print(f"{name} is a {profession}")
        else:
            print(f"User {name} not found in the database")


User.print_user_info("Alice")  # Alice is a Programmer


class User:
    def __init__(self, name):
        self.name = name
        self.user_infos = {
            "Alice": "Programmer", "Bob": "Data Scientist"
        }

    def get_profession(self):
        return self.user_infos.get(self.name)

    def print_user_info(self):
        profession = self.get_profession()  # インスタンスメソッドの呼び出し
        if profession:
            print(f"{self.name} is a {profession}")
        else:
            print(f"User {self.name} not found in the database")


user = User("Alice")
user.print_user_info()  # Alice is a Programmer


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(5, 3))  # 8
print(Calculator.multiply(5, 3))  # 15
