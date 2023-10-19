class Employee:  # クラス定義

    company = "インプレス"  # クラス変数

    def __init__(self, name, position):  # コンストラクタ
        self.name = name  # インスタンス変数
        self.position = position  # インスタンス変数


print(Employee.company)  # インプレスと表示
# インスタンスの生成
employee1 = Employee("Alice", "Engineer")
employee2 = Employee("Bob", "Researcher")

# インスタンス変数とクラス変数へのアクセス
print(employee1.name)  # Alice
print(employee1.company)  # インプレス

print(employee2.name)  # Bob
print(employee2.company)  # インプレス

Employee.company = "Impress"  # クラス名を指定してクラス変数を変更する
print(employee1.company)  # Impress
print(employee2.company)  # Impress
