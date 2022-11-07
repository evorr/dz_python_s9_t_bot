def get_numbers(command_str):
    data_list = command_str.split(' ')
    if data_list[1].isdigit() and data_list[2].isdigit():
        numb_1 = int(data_list[1])
        numb_2 = int(data_list[2])
    else:
        numb_1 = complex(data_list[1])
        numb_2 = complex(data_list[2])
    return numb_1, numb_2


def sum_num(x, y):
    return x + y


def sub_num(x, y):
    return x - y


def mult_num(x, y):
    return x * y


def div_num(x, y):
    return x / y
