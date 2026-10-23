import random
from typing import Generator
from itertools import islice


def inf_in_range(start: int, end: int) -> Generator[int, None, None]:
    """Генерирует бесконечное число случайных целых чисел в диапазоне от 
    start до end."""
    while True:
        yield random.randint(start, end)


if __name__ == "__main__":
    gen = inf_in_range(1, 100)

    first_five = list(islice(gen, 5))
    print(first_five)
