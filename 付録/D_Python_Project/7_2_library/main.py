# main.py
from subfolder import Calculator
from subfolder.module1 import greet, Calculator
import mymodule

# mymoduleのhello関数を使用
mymodule.hello("Alice")  # Heelo, Alice

# mymoduleのMyClassを使用
obj = mymodule.MyClass(123)
obj.display()  # Value: 123


# 'greet' 関数を使用
print(greet("Alice"))  # Output: Hello, Alice!

# 'Calculator' クラスを使用
calc = Calculator()
print(calc.add(5, 3))  # Output: 8


# 'Calculator' クラスを使用
calc = Calculator()
print(calc.add(5, 3))  # Output: 8
