class Guard:
    def __init__(self):
        self.timeAsleep = 0
        self.dayTiming = []
        for i in range(0, 60):
            self.dayTiming.append(0)


def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def pre_process(input_list):
    input_list.sort()
    guards = {}
    current_id = 0
    minute_asleep = 0
    for inp in input_list:
        if "begins shift" in inp:
            current_id = int(inp[inp.index('#') + 1:inp.index(" b")])
            if current_id not in guards:
                guards[current_id] = Guard()
        elif "falls asleep" in inp:
            minute_asleep = int(inp[inp.index(':') + 1:inp.index(']')])
        elif "wakes up" in inp:
            minute_awake = int(inp[inp.index(':') + 1:inp.index(']')])
            delta = minute_awake - minute_asleep
            guards[current_id].timeAsleep += delta
            for i in range(minute_asleep, minute_awake):
                guards[current_id].dayTiming[i] += 1
    return guards


def first_part(guards):
    max_asleep = 0
    max_asleep_id = 0
    timing = 0
    hour_timing = 0
    for guard_id, guard in guards.items():
        if max_asleep == 0 or max_asleep < guard.timeAsleep:
            max_asleep = guard.timeAsleep
            max_asleep_id = guard_id
            for i in range(0, len(guard.dayTiming)):
                if timing < guard.dayTiming[i]:
                    timing = guard.dayTiming[i]
                    hour_timing = i
    return hour_timing * max_asleep_id


def second_part(guards):
    timing = 0
    hour_timing = 0
    guard_id_timing = 0
    for guard_id, guard in guards.items():
        for i in range(0, len(guard.dayTiming)):
            if timing < guard.dayTiming[i]:
                timing = guard.dayTiming[i]
                hour_timing = i
                guard_id_timing = guard_id
    return guard_id_timing * hour_timing


lst = read_input("input")
guards_list = pre_process(lst)
print(first_part(guards_list))
print(second_part(guards_list))
