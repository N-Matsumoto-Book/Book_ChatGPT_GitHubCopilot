class Employee:  # 親クラス
    base_salary = 10000

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def calculate_salary(self):
        return Employee.base_salary

    def print_info(self):
        print(f"name: {self.name}, age: {self.age}, address: {self.address}")


class FullTimeEmployee(Employee):  # 子クラス
    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary

    def calculate_salary(self):  # メソッドのオーバーライド
        return self.salary


class PartTimeEmployee(Employee):  # 子クラス
    def __init__(self, name, age, address, hourly_rate, hours_worked):
        super().__init__(name, age, address)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):  # メソッドのオーバーライド
        return self.hourly_rate * self.hours_worked


# FullTimeEmployee インスタンス作成
full_time_employee = FullTimeEmployee("山田太郎", 30, "御堂筋123", 5000000)
full_time_employee.print_info()  # name: 山田太郎, age: 30, address: 御堂筋123
full_time_employee = FullTimeEmployee("山田太郎", 30, "御堂筋123", 5000000)
print(full_time_employee.calculate_salary())  # 5000000(self.salaryの値を表示)

employee = Employee("山田太郎", 30, "御堂筋123")
print(employee.calculate_salary())  # 10000(base_salaryの値)
# 子クラス(FullTimeEmployee, ParTimeEmployee)のインスタンスを作成します
full_time_employee = FullTimeEmployee("John Doe", 30, "123 Main St", 50000)
part_time_employee = PartTimeEmployee("Jane Doe", 25, "456 Elm St", 20, 20)

# それぞれの従業員を含むリストを作成します
employees = [full_time_employee, part_time_employee]

# employeesをループさせます。
for employee in employees:
    print(employee.calculate_salary())  # 子クラスのcalculate_salaryを実行
