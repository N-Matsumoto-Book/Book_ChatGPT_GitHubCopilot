from typing import List, Dict, Tuple


def greet(name: str) -> str:
    return "Hello, " + name


print(greet("Alice"))  # Output: Hello, Alice


def data_summary(data: List[int]) -> Tuple[int, float]:
    total = sum(data)
    average = total / len(data)
    return total, average


print(data_summary([10, 20, 30, 40]))  # Output: (100, 25.0)
