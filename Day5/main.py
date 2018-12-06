def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def first_part(str_input):
    magic_number = 32
    result = str_input
    break_loop = False
    while not break_loop:
        for i in range(0, len(result) - 1):
            if result[i] != result[i + 1] and abs(ord(result[i]) - ord(result[i + 1])) == magic_number:
                result = result[:i] + result[i + 2:]
                break_loop = False
                break
            break_loop = True
    return len(result)


def second_part(str_input):
    ascii_start = 65
    ascii_end = 90
    magic_number = 32
    minimum = len(str_input)
    for i in range(ascii_start, ascii_end + 1):
        result = str_input.replace(chr(i), '')
        result = result.replace(chr(i + magic_number), '')
        minimum = min(first_part(result), minimum)
    return minimum


lst = read_input("input")[0]
print(first_part(lst))
print(second_part(lst))
