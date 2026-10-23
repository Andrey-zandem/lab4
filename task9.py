import random
from typing import Generator


def random_in_range(start: int, end: int, count: int) -> Generator[int, None, None]:
    """Генерирует count случайных целых чисел в диапазоне от start до end."""
    for _ in range(count):
        yield random.randint(start, end)


if __name__ == "__main__":
    gen = random_in_range(1, 100, 5)

    for num in gen:
        print(num)
