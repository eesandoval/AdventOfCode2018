initial_state = ""
decisions = {}


def read_input(filename):
    global initial_state
    global decisions 
    with open(filename) as file:
        lines = file.readlines()
    initial_state = lines[0][15:].strip()
    for i in range(2, len(lines)):
        key = lines[i][0:5]
        value = lines[i][9]
        if value == '#':
            value = True
        else:
            value = False
        decisions[key] = value 
    return


def first_part(generations=20):
    global initial_state 
    global decisions
    padded_index = generations
    new_state = list((".") * padded_index + initial_state + ("." * padded_index)) 
    current_state = list((".") * padded_index + initial_state + ("." * padded_index)) 
    for _ in range(1, generations + 1):
        for index in range(2, len(current_state) - 3):
            key = ''.join(current_state[index - 2:index + 3])
            if key in decisions and decisions[key]:
                new_state[index] = '#'
            else:
                new_state[index] = '.'
        current_state = new_state[:]
    result = 0
    for pot in range(0, len(current_state)):
        if current_state[pot] == '#':
            result += pot - padded_index
    return result


def second_part():
    last_answer = first_part()
    delta_anwer = 0
    last_delta = 0
    delta_count = 0
    i = 21
    for i in range(21, 2000):
        new_answer = first_part(i)
        delta_anwer = new_answer - last_answer
        if delta_anwer == last_delta:
            delta_count += 1
        else:
            delta_count = 0
        if delta_count > 4:
            break
        last_answer = new_answer
        last_delta = delta_anwer
    return (50000000000 - i) * delta_anwer + new_answer


read_input("input")
print(first_part())
print(second_part())
