class Node:
    def __init__(self, children_count, metadata_count, children, metadata):
        self.children_count = int(children_count)
        self.metadata_count = int(metadata_count)
        self.children = children
        self.metadata = metadata

    def count_nodes(self):
        result = self.metadata_count + 2
        for c in self.children:
            result += c.count_nodes()
        return result

    def count_metadata(self):
        result = 0
        for m in self.metadata:
            result += m
        for c in self.children:
            result += c.count_metadata()
        return result

    def get_value(self):
        result = 0
        if self.children_count == 0:
            for m in self.metadata:
                result += m
        else:
            for m in self.metadata:
                if m > self.children_count:
                    continue
                index_m = m - 1
                result += self.children[index_m].get_value()
        return result


def read_input(filename):
    with open(filename) as file:
        result = file.readlines()[0].split()
    return result


def pre_process(input_list):
    def traverse(current_node, input_lst, input_i):
        for k in range(0, current_node.children_count):
            new_node = traverse(Node(input_lst[input_i], input_lst[input_i + 1], [], []), input_lst, input_i + 2)
            input_i += new_node.count_nodes()
            current_node.children.append(new_node)
        for k in range(0, current_node.metadata_count):
            current_node.metadata.append(int(input_lst[input_i + k]))
        return current_node

    result = Node(input_list[0], input_list[1], [], [])
    traverse(result, input_list, 2)
    return result


def first_part(tree):
    return tree.count_metadata()


def second_part(tree):
    return tree.get_value()


lst = read_input("input")
t = pre_process(lst)
print(first_part(t))
print(second_part(t))
