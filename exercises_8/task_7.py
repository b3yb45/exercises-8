import json


def to_json(func):
    def inner(x):
        return json.dumps(func(x))

    return inner


@to_json
def num_squares(n):
    return {x: x ** 2 for x in range(0, n)}


@to_json
def num_len_list(n):
    return [len(str(x)) for x in range (0, n)]


print(num_squares(5))
print(type(num_squares(5)))
print(num_len_list(20))
print(type(num_len_list(20)))
