def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def first_part(input_list):
    count_two = 0
    count_three = 0
    for i in input_list:
        match_two = 0
        match_three = 0
        for ascii_char in range(97, 123):
            if i.count(chr(ascii_char)) == 2:
                match_two = 1
            elif i.count(chr(ascii_char)) == 3:
                match_three = 1
        count_two += match_two
        count_three += match_three
    return count_two * count_three


def second_part(input_list):
    result = ""
    for i in range(0, len(input_list) - 1):
        for j in range(i, len(input_list)):
            strikeout = 0
            diff = -1
            for c in range(0, len(input_list[i])):
                if input_list[i][c] != input_list[j][c]:
                    strikeout += 1
                    diff = c
                if strikeout > 1:
                    break
            if strikeout == 1:
                result = input_list[i][:diff] + input_list[i][diff + 1:]
                break
        if result != "":
            break
    return result


lst = read_input("input")
print(first_part(lst))
print(second_part(lst))
