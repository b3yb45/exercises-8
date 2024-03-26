import time


def limit_execution_time(max_seconds, max_calls):
    def decorator(func):
        call_count = 0
        start_time = time.time()

        def wrapper(*args, **kwargs):
            nonlocal call_count, start_time
            elapsed_time = time.time() - start_time

            if call_count >= max_calls or elapsed_time >= max_seconds:
                raise Exception("Limit exceeded")

            call_count += 1
            return func(*args, **kwargs)

        return wrapper
    return decorator


@limit_execution_time(5, 10)
def some_function():
    time.sleep(1)


for _ in range(4):
    some_function()
print('-------')


for _ in range(20):
    some_function()
print('-------')
