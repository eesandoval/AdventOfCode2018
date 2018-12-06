id_claim = {}


def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def process_input(input_list, board_rows=1000, board_cols=1000):
    result = []
    for r in range(0, board_rows):
        row = []
        for c in range(0, board_cols):
            row.append('.')
        result.append(row)
    for i in input_list:
        input_id = i[1:i.find('@') - 1]
        start_col = int(i[i.find('@') + 2:i.find(',')])
        start_row = int(i[i.find(',') + 1:i.find(':')])
        len_col = int(i[i.find(':') + 2:i.find('x')])
        len_row = int(i[i.find('x') + 1:])
        id_claim[input_id] = True
        for row in range(start_row, start_row + len_row):
            for col in range(start_col, start_col + len_col):
                if result[row][col] == '.':
                    result[row][col] = input_id
                else:
                    id_claim[input_id] = False
                    if result[row][col] != 'X':
                        id_claim[result[row][col]] = False
                    result[row][col] = 'X'
    return result


def first_part(fabric):
    result = 0
    for r in range(0, len(fabric)):
        for c in range(0, len(fabric[r])):
            if fabric[r][c] == 'X':
                result += 1
    return result


def second_part(claims):
    for claim_id, claim in claims.items():
        if claim:
            return claim_id


lst = read_input("input")
board = process_input(lst)
print(first_part(board))
print(second_part(id_claim))
