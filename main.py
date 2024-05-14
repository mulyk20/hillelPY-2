def longer_string(str1: str, str2: str) -> str:
    """Повертає довшу з двох заданих стрічок."""
    return max(str1, str2, key=len)


def only_numbers(lst: list) -> bool:
    """Перевіряє, чи список складається тільки з чисел."""
    return all(isinstance(item, int) for item in lst)


def print_line() -> None:
    """Виводить в консоль рядок '*' * 80."""
    print("*" * 80)


# Приклади використання:

# Поверне "world"
print(longer_string("hello", "worlds"))

# Поверне False
print(only_numbers(["hello", 123, True]))

# Виведе рядок '*' * 80
print_line()
