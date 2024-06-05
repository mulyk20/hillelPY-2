from functools import wraps
from typing import Any, Callable


def filter_list_decorator(remove_type: str):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                if remove_type == "str":
                    result = [item for item in result if not isinstance(item, str)]
                elif remove_type == "int":
                    result = [item for item in result if not isinstance(item, int)]
                elif remove_type == "float":
                    result = [item for item in result if not isinstance(item, float)]
            return result

        return wrapper

    return decorator


@filter_list_decorator("str")
def generate_list_with_strings() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_list_decorator("int")
def generate_list_with_integers() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_list_decorator("float")
def generate_list_with_floats() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_list_decorator("none")
def generate_list_with_none() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_list_decorator("str")
def return_non_list() -> Any:
    return "This is not a list"


print(generate_list_with_strings())
print(generate_list_with_integers())
print(generate_list_with_floats())
print(generate_list_with_none())
print(return_non_list())
