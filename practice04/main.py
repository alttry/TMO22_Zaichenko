print("Задание 1")
x = 18

def show():
    x = 8
    print(x)

show()
print(x)

# Внутри функции show() используется локальная переменная x = 8
# а снаружи используется глобальная переменная x = 18

print("Задание 2")
def total(*args):
    return sum(args)

print(total(8, 9, 10))

print("Задание 3")
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Илья", age=19))

print("Задание 4")
def increase(x):
    return x + 3

def apply(func, value):
    return func(value)

print(apply(increase, 5))

print("Задание 5")
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
