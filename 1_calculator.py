print("(1) 더하기  (2) 빼기  (3) 나누기  (4) 곱하기")
select = int(input("select: "))

first = int(input("first number: "))
second = int(input("second number: "))


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def divide(a, b):
    return a // b


def multiply(a, b):
    return a * b


if select == 1:
    print("answer: ", plus(first, second))

elif select == 2:
    print("answer: ", minus(first, second))

elif select == 3:
    print("answer: ", divide(first, second))

elif select == 4:
    print("answer: ", multiply(first, second))
