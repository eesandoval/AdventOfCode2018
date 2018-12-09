class LinkedList:
    def __init__(self, value, previous=None, next_node=None):
        self.next = next_node
        self.previous = previous
        self.value = value

    def insert(self, new_value):
        new_node = LinkedList(new_value, self, self.next)
        self.next.previous = new_node
        self.next = new_node

    def remove(self):
        self.previous.next = self.next
        self.next.previous = self.previous
        return self.next


def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()[0]
    result = (int(lines[0:lines.index("players") - 1]), int(lines[lines.index("worth") + 6:lines.index("points") - 1]))
    return result


def play_game(players, points):
    list_points = [0 for _ in range(0, players)]
    marbles = [x for x in range(0, points + 1)]
    game = LinkedList(marbles[0])
    marbles = marbles[1:]
    game.next = game
    game.previous = game
    marble_index = 0
    while True:
        for player in range(0, len(list_points)):
            if marbles[marble_index] % 23 == 0:
                for _ in range(0, 8):
                    game = game.previous
                list_points[player] += marbles[marble_index] + game.value
                game = game.remove()
                game = game.next
            else:
                game.insert(marbles[marble_index])
                game = game.next.next
            marble_index += 1
            if marble_index >= len(marbles):
                return list_points


def first_part(players, points):
    return max(x for x in play_game(players, points))


def second_part(players, points):
    new_points = points * 100
    return max(x for x in play_game(players, new_points))


players_points = read_input("input")
print(first_part(players_points[0], players_points[1]))
print(second_part(players_points[0], players_points[1]))
