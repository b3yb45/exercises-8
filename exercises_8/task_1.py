IN_STRING = 'aAgGIiHhkfOOO'
I = 1
J = 6


def filter_upper(in_char):
    if in_char.isupper():
        return True
    return False


upper_quant = len(list(filter(filter_upper, IN_STRING[I-1:J-1])))
print(upper_quant)
