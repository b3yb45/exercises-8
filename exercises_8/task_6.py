def one_arg_decor(func):
    def inner(x):
        print(func(x))

    return inner


@one_arg_decor
def greet(name):
    return f'hello {name}'


@one_arg_decor
def mult_by_3(num):
    return num * 3


greet('Ivan')
mult_by_3(5)
