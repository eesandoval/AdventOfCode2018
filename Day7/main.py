def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def parse_input(step_list, steps, input_list):
    for i in input_list:
        step_name = i[36]
        step_pre = i[5]
        steps.add(step_name)
        steps.add(step_pre)
        if step_name in step_list.keys():
            step_list[step_name].add(step_pre)
        else:
            step_list[step_name] = {step_pre}


def first_steps(step_list, steps):
    next_steps = []
    for step in steps:
        if step not in step_list.keys():
            next_steps.append(step)
    next_steps.sort()
    return next_steps


def first_part(input_list):
    step_list = {}
    steps = set()
    parse_input(step_list, steps, input_list)
    result = ""
    next_step = ""
    steps = sorted(steps)
    next_steps = first_steps(step_list, steps)
    while True:
        result += next_step
        for key in step_list.keys():
            if next_step in step_list[key]:
                step_list[key].remove(next_step)
                if len(step_list[key]) == 0:
                    next_steps.append(key)
        if next_step in next_steps:
            next_steps.remove(next_step)
        if len(result) == len(steps):
            return result
        next_steps.sort()
        next_step = next_steps[0]


def second_part(input_list, duration, workers):
    def find_next_steps(completed_steps_set, step_list_lst, next_steps_lst):
        for completed_step in completed_steps_set:
            for key in step_list_lst.keys():
                if completed_step in step_list_lst[key]:
                    step_list_lst[key].remove(completed_step)
                    if len(step_list_lst[key]) == 0:
                        next_steps_lst.append(key)
            if completed_step in next_steps_lst:
                next_steps_lst.remove(completed_step)
        next_steps_lst.sort()

    def get_step_worker(working_on_lst, worker_int, next_steps_lst, duration_int):
        working_on[worker_int] = next_steps[0]
        result_lst = next_steps_lst[1:]
        time_left[worker_int] = ord(working_on_lst[worker_int]) - 65 + duration_int
        return result_lst

    step_list = {}
    steps = set()
    parse_input(step_list, steps, input_list)
    result = ""
    steps = sorted(steps)
    next_steps = first_steps(step_list, steps)
    time = -1
    working_on = {}
    time_left = {}
    for i in range(0, workers):
        working_on[i] = ''
        time_left[i] = 0
    while True:
        completed_steps = set()
        for worker in working_on:
            if working_on[worker] == '' and len(next_steps) > 0:
                next_steps = get_step_worker(working_on, worker, next_steps, duration)
            elif working_on[worker] != '':
                time_left[worker] -= 1
                if time_left[worker] == 0:
                    completed_steps.add(working_on[worker])
                    result += working_on[worker]
                    working_on[worker] = ''
                    time_left[worker] = 0
                    find_next_steps(completed_steps, step_list, next_steps)
                    if len(next_steps) > 0:
                        next_steps = get_step_worker(working_on, worker, next_steps, duration)
                    if len(next_steps) > 0:
                        for sub_worker in working_on.keys():
                            if working_on[sub_worker] == '' and len(next_steps) > 0:
                                next_steps = get_step_worker(working_on, sub_worker, next_steps, duration)
        find_next_steps(completed_steps, step_list, next_steps)
        time += 1
        if len(result) == len(steps):
            return time


lst = read_input("input")
print(first_part(lst))
print(second_part(lst, 61, 5))
