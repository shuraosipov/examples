import secrets
import string
import time
import functools


def timer(func):
    """Print the run time of the decorated function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function {func.__name__!r} finished in {run_time:.4f} secs")
        return value

    return wrapper


@timer
def generate_string(length=8) -> str:
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


print(generate_string(length=12))

waste_some_time(999)
