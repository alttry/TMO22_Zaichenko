# вариант 8
# задание 1
g = (x + 8 for x in [1, 2, 3])
print(list(g))


# задание 2
def announce(func):
    def wrapper():
        result = func()
        print("Запуск")
        return result
    return wrapper

@announce
def hello():
    print("привет")

hello()