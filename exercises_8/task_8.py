import datetime

now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def exception_decor(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            with open('error_log.txt', 'a') as f:
                f.write(f"{now} [Error]: {e} \n")

    return inner


@exception_decor
def division(a, b):
    return a / b


@exception_decor
def file_write(file, data):
    with open(file, 'w') as f:
        f.write(data)


print(division(5, 0))
print(file_write('test7.txt', 2))
