def do_something(start: int, end: int) -> None:
    multiples_of_three: List[int] = []
    for num in range(start, end):
        if num % 3 == 0:
            multiples_of_three.append(num)
    multiples_of_three = [num * 3 for num in multiples_of_three]
    result: int = sum(multiples_of_three)
    print(result)


do_something(1, 15)
