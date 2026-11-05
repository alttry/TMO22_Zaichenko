def grams_per_portion(grams, portions):
    if portions == 0:
        return "На ноль делить нельзя"
    return grams / portions

# Проверка
assert grams_per_portion(900, 6) == 150.0
assert grams_per_portion(900, 0) == "На ноль делить нельзя"
assert grams_per_portion(300, 2) == 150.0

# Сортировка слов по длине с помощью lambda
words = ["сон", "завтрак", "тренировка"]
sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)