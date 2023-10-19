# カプセル化されていない例
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


account = BankAccount("John Doe", 500)  # インスタンスを作成
print(account.balance)  # 属性balanceにアクセスできてしまう


class BankAccount:
    def __init__(self, name, balance):
        self.__name = name  # プライベート変数
        self.__balance = balance  # プライベート変数


account = BankAccount("John Doe", 500)  # インスタンスを作成
# AttributeError 'BankAccount' object has no attribute '__balance'
# print(account.__balance)


class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def balance(self):  # プロパティを宣言
        print("Balanceを取得")  # 「Balanceを取得」と表示
        return self.__balance  # プライベート変数__balanceの値を返す


account = BankAccount("John Doe", 500)  # インスタンスを作成
print(account.balance)  # Balanceを取得, 500を表示(ゲッターを呼び出す)


class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property  # ゲッターを宣言
    def balance(self):
        print("Getting balance")  # Getting balance
        return self.__balance  # プライベート変数__balanceの値を返す

    @balance.setter  # セッターを宣言
    def balance(self, amount):
        self.__balance = amount  # 新しい値を__balanceに設定する


account = BankAccount("John Doe", 500)  # インスタンスを作成
account.balance = 1000  # セッターを呼び出す
print(account.balance)  # 1000(ゲッターを呼び出す)


class BankAccount:
    def __init__(self, name, balance):
        self.__name = name  # プライベート変数
        self.__balance = balance  # プライベート変数

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("預け入れには、正の金額を入れてください")
        self.__balance = amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("引き出す金額は0よりも大きくしてください")
        self.balance -= amount  # インスタンスメソッドからプライベート変数にアクセスして更新


try:
    account = BankAccount("Taro", 100)  # __balanceを100として設定
    account.withdraw(200)  # ValueError
except ValueError as e:
    pass
print(account.balance)  # コンストラクタで設定した100がそのまま表示される
