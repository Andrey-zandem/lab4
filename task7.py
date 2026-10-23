import functools
from typing import Any, Callable


def log_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Завершение функции {func.__name__}")
        return result

    return wrapper


@log_decorator
def hello() -> None:
    print("Hello, world!")


hello()
