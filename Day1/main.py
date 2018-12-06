def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def first_part(input_list):
    result = '0'
    for i in input_list:
        result = str(eval(result + i))
    return result


def second_part(input_list):
    result = '0'
    out_list = {'0'}
    break_loop = False
    while not break_loop:
        for i in input_list:
            result = str(eval(result + i))
            if result in out_list:
                break_loop = True
                break
            out_list.add(result)
    return result


lst = read_input("input")
print(first_part(lst))
print(second_part(lst))
